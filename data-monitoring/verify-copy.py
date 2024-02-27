#!/usr/bin/env python3

import sys
from os import listdir, makedirs, system
from os.path import join, isdir, isfile, splitext

import shutil
import pandas as pd
import re
import math
import subprocess
from collections import defaultdict

class c:
    RED = '\033[31m'
    GREEN = '\033[32m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def allowed_val(allowed_vals, value):
    allowed_vals = allowed_vals.replace(" ", "")
    intervals = re.split("[\[\]]", allowed_vals)
    intervals = list(filter(lambda x: x not in [",", ""], intervals))
    allowed = False
    for interval in intervals:
        lower = float(interval.split(",")[0])
        upper = float(interval.split(",")[1])
        if lower <= int(value) <= upper:
            allowed = True
            break
    return allowed

def check_number_of_files(path, datatype, tasks, corrected):
    if corrected:
        print("deviation.txt seen in ", path, ", continuing.")
        return
    for raw_file in listdir(path):
        file_re = re.match('^sub-([0-9]{7})_(.*)_(s[0-9]+_r[0-9]+_e[0-9]+)\.([a-z0-9.]+)$', raw_file)
        if re.match('^[Dd]eviation$', raw_file):
            print("deviation.txt seen in", path, ", continuing.")
            return
        if not file_re:
            print("unexpected file format seen in", join(path, raw_file))
        if file_re and file_re.group(2) not in tasks:
            print("unexpected task name seen in", join(path, raw_file))
    taskssum = 0
    already_counted = []
    for task in tasks:
        comb = False
        for row in combination_rows.keys():
            if task in already_counted:
                comb = True
                break
            if task in combination_rows[row] and row not in already_counted:
                comb = True
                already_counted.extend(combination_rows[row])
                taskssum += len(dd_dict[task][2].split(",")) # number files expected from expectedFileExt # assume combination rows expect same # files
                break
        if not comb:
            # not a combination row
            taskssum += len(dd_dict[task][2].split(",")) # number files expected from expectedFileExt
    obs_files = len(listdir(path))
    if obs_files > taskssum:
        print(c.RED + "Error: number of", datatype, "data files in subject folder", sub, str(obs_files), "greater than the expected number", str(taskssum) + c.ENDC)
    if obs_files < taskssum:
        print(c.RED + "Error: number of", datatype, "data files in subject folder", sub, str(obs_files), "less than the expected number", str(taskssum) + c.ENDC)
    tasks_seen = []
    for raw_file in listdir(path):
        file_re = re.match('^sub-([0-9]+)_(.*)_(s[0-9]+_r[0-9]+_e[0-9]+)\.([a-z0-9]+)$', raw_file)
        if file_re and file_re.group(2) not in tasks_seen:
            tasks_seen.append(file_re.group(2))
    for key in combination_rows.keys():
        combination_rows_seen = set(tasks_seen).intersection(set(combination_rows[key]))
        if len(combination_rows_seen) > 1:
            print(c.RED + "Error: multiple different combination rows", str(combination_rows_seen), "seen in subject folder", sub, ": ", str(path), ", only one expected." + c.ENDC)

def check_filenames(path, sub, ses, datatype, allowed_suffixes, possible_exts, numfiles, var, corrected):
        task_files_counter = defaultdict(lambda: 0)
        task_names = []
        for raw_file in listdir(path):
            for task in task_vars:
                if re.match('^sub-([0-9]{7})_('+task +')_(s[0-9]+_r[0-9]+_e[0-9]+)\.([a-z0-9.]+)$', raw_file):
                    if task not in task_names:
                        task_names.append(task)
                    task_files_counter[task] += 1
        if corrected:
            print("deviation.txt seen in ", path, ", continuing.")
            for raw_file in listdir(path):
                # still check that files are in the correct subject folder and session folder
                file_re = re.match("^(sub-[0-9]*)_([a-zA-Z0-9_-]*_)?(s[0-9]*_r[0-9]*)_e[0-9]*.*$", raw_file)
                if file_re and file_re.group(1) != sub:
                    print(c.RED + "Error: file from subject", file_re.group(1), "found in", sub, "folder:", path + c.ENDC)
                if file_re and len(ses) > 0 and file_re.group(3) != ses:
                    print(c.RED + "Error: file from session", file_re.group(3), "found in", ses, "folder:", path + c.ENDC)
            return
        for raw_file in listdir(path):
            #check sub-#, check session folder, check extension
            file_re = re.match("^(sub-([0-9]*))_([a-zA-Z0-9_-]*)_((s([0-9]*)_r([0-9]*))_e([0-9]*))((?:\.[a-zA-Z]+)*)$", raw_file)
            if file_re:
                if file_re.group(1) != sub:
                    print(c.RED + "Error: file from subject", file_re.group(1), "found in", sub, "folder:", join(path, raw_file) + c.ENDC)
                if file_re.group(5) != ses and len(ses) > 0:
                    print(c.RED + "Error: file from session", file_re.group(5), "found in", ses, "folder:", join(path, raw_file) + c.ENDC)
                if file_re.group(9) not in possible_exts and len(file_re.group(9)) > 0:
                    print(c.RED + "Error: file with extension", file_re.group(9), "found, doesn\'t match expected extensions", ", ".join(possible_exts), ":", join(path, raw_file) + c.ENDC)
                if file_re.group(2) != '' and not allowed_val(allowed_subs, file_re.group(2)):
                    print(c.RED + "Error: subject number", file_re.group(2), "not an allowed subject value", allowed_subs, "in file:", join(path, raw_file) + c.ENDC)
                if file_re.group(3) not in dd_dict.keys():
                    print(c.RED + "Error: variable name", file_re.group(3), "does not match any datadict variables, in file:", join(path, raw_file) + c.ENDC)
                if datatype not in file_re.group(3):
                    print(c.RED + "Error: variable name", file_re.group(3), "does not contain the name of the enclosing datatype folder", datatype, "in file:", join(path, raw_file) + c.ENDC)
                if file_re.group(4) not in allowed_suffixes:
                    print(c.RED + "Error: suffix", file_re.group(4), "not in allowed suffixes", ", ".join(allowed_suffixes), "in file:", join(path, raw_file) + c.ENDC)
                if file_re.group(2) == "":
                    print(c.RED + "Error: subject # missing from file:", join(path, raw_file) + c.ENDC)
                if file_re.group(3) == "":
                    print(c.RED + "Error: variable name missing from file:", join(path, raw_file) + c.ENDC)
                if file_re.group(6) == "":
                    print(c.RED + "Error: session # missing from file:", join(path, raw_file) + c.ENDC)
                if file_re.group(7) == "":
                    print(c.RED + "Error: run # missing from file:", join(path, raw_file) + c.ENDC)
                if file_re.group(8) == "":
                    print(c.RED + "Error: event # missing from file:", join(path, raw_file) + c.ENDC)
                if file_re.group(9) == "":
                    print(c.RED + "Error: extension missing from file, does\'nt match expected extensions", ", ".join(possible_exts), ":", join(path, raw_file) + c.ENDC)
                if datatype == "psychopy" and file_re.group(9) == ".csv" and file_re.group(2) != "":
                    # Call check-id.py for psychopy files
                    subprocess.run(["python3", "check-id.py", file_re.group(2), join(path, raw_file)], shell=False)
            else:
                print(c.RED + "Error: file ", join(path, raw_file), " does not match naming convention <sub-#>_<variable/task-name>_<session>.<ext>" + c.ENDC)
        combination = False
        for dict_var, values in combination_rows.items():
            if var in values:
                combination = True
                combination_var = dict_var
                break
        for ext in possible_exts:
            file_present = False
            for ext2 in ext.split("|"): # in case of multiple options for extensions i.e. .zip.gpg|.tar.gpg
                for suf in allowed_suffixes:
                    #if combination:
                        # combination_file_present = False
                        # for eitheror_var in combination_rows[combination_var]:
                        #     if isfile(join(path, sub+'_'+eitheror_var+'_'+suf+ext2)):
                        #         if combination_file_present:
                        #             second_file_seen = sub+'_'+eitheror_var+'_'+suf+ext2
                        #             print(c.RED + "Error: both", file_seen, "and", second_file_seen, "found in", path + ", should have only one or the other" + c.ENDC)
                        #         else:
                        #             file_present = True
                        #             combination_file_present = True
                        #             file_seen = sub+'_'+eitheror_var+'_'+suf+ext2
                    if combination:
                        for eitheror_var in combination_rows[combination_var]:
                            if isfile(join(path, sub+'_'+eitheror_var+'_'+suf+ext2)):
                                file_present = True
                                break
                    else:
                        if isfile(join(path, sub+'_'+var+'_'+suf+ext2)):
                            file_present = True
                            break
            if not file_present:
                print(c.RED + "Error: no such file", sub+'_'+var+'_sX_rX_eX'+ext, "can be found in", path + c.ENDC)

if __name__ == "__main__":
    dataset = sys.argv[1]

    raw = join(dataset,"sourcedata","raw")
    checked = join(dataset,"sourcedata","checked")

    datadict = "{}/data-monitoring/data-dictionary/central-tracker_datadict.csv".format(dataset)

    sessions = False
    for dir in listdir(join(dataset,"sourcedata","raw")):
        if re.match("s[0-9]+_r[0-9]+(_e[0-9]+)?", dir):
            sessions = True
            break

    df_dd = pd.read_csv(datadict, index_col = "variable")
    dd_dict = dict()

    task_vars = []
    combination_rows = {}
    for _, row in df_dd.iterrows():
        if not isinstance(row["expectedFileExt"], float):
            task_vars.append(row.name)
        if row["dataType"] == "combination":
            idx = row["provenance"].split(" ").index("variables:")
            vars = "".join(row["provenance"].split(" ")[idx+1:]).split(",")
            vars = [var.strip("\"") for var in vars]
            combination_rows[row.name] = vars

    # build dict of expected files/datatypes from datadict
    for var, row in df_dd.iterrows():
        if row.name in task_vars:
            dd_dict[var] = [row["dataType"], row["allowedSuffix"], row["expectedFileExt"], row["allowedValues"]]

    allowed_subs = df_dd.loc["id", "allowedValues"]

    # now search sourcedata/raw for correct files
    for variable, values in dd_dict.items():
        print("Verifying files in raw for:", variable)
        datatype = values[0]
        allowed_suffixes = values[1].split(", ")
        fileexts = values[2].split(", ") # with or without . ?
        allowed_vals = values[3].split(", ")
        possible_exts = sum([ext.split('|') for ext in fileexts], [])
        numfiles = len(fileexts)

        if sessions:
            expected_sessions = []
            for ses in allowed_suffixes:
                ses_re = re.match("(s[0-9]+_r[0-9]+)(_e[0-9]+)?", ses)
                if ses_re:
                    expected_sessions.append(ses_re.group(1))
        else:
            expected_sessions = [""]
        for ses in expected_sessions:
            if isdir(join(raw, ses, datatype)):
                for subject in listdir(join(raw, ses, datatype)):
                    if not re.match("^sub-[0-9]+$", subject):
                        print(c.RED + "Error: subject directory ", subject, " does not match sub-# convention" + c.ENDC)
                        continue
                    path = join(raw, ses, datatype, subject)
                    # check that files in raw match conventions
                    corrected = False
                    for raw_file in listdir(path):
                        if re.match('^[Dd]eviation.*$', raw_file):
                            corrected = True
                            break
                    check_filenames(path, subject, ses, datatype, allowed_suffixes, possible_exts, numfiles, variable, corrected)
                    # copy to checked
                    for suffix in allowed_suffixes:
                        presence = False
                        copied_files = []
                        for req_ext in fileexts:
                            for ext in req_ext.split('|'):
                                for raw_file in listdir(join(raw, ses, datatype, subject)):
                                    if re.match(subject + "_" + variable + "_" + suffix + ext, raw_file):
                                        presence = True
                                        # copy file to checked, unless "deviation" is seen
                                        if not isdir(join(checked, subject, ses, datatype)):
                                            print(c.GREEN + "Creating ", join(subject, ses, datatype), " directory in checked" + c.ENDC)
                                            makedirs(join(checked, subject, ses, datatype))
                                        if not isfile(join(checked, subject, ses, datatype, raw_file)) and splitext(raw_file)[1] != '.gpg':
                                            print(c.GREEN + "Copying ", raw_file, " to checked" + c.ENDC)
                                            system('cp -p ' + join(raw, ses, datatype, subject, raw_file) + ' ' + join(checked, subject, ses, datatype, raw_file))
                                        copied_files.append(raw_file)
            else:
                print(c.RED + "Error: can\'t find", datatype, "directory under", raw+"/"+ses + c.ENDC)
    print("Verifying numbers of files in subdirectories in raw")
    datatype_folders = []
    for subdir in dd_dict.values():
        if subdir[0] not in datatype_folders:
            datatype_folders.append(subdir[0])
    for session_folder in listdir(raw):
        if isdir(join(raw, session_folder)):
            for datatype_folder in datatype_folders:
                tasks = []
                for task, vals in dd_dict.items():
                    if vals[0] == datatype_folder:
                        tasks.append(task)
                if isdir(join(raw, session_folder, datatype_folder)):
                    for sub in listdir(join(raw, session_folder, datatype_folder)):
                        path = join(raw, session_folder, datatype_folder, sub)
                        corrected = False
                        for raw_file in listdir(path):
                            if re.match('^[Dd]eviation.*$', raw_file):
                                corrected = True
                                break
                        check_number_of_files(path, datatype_folder, tasks, corrected)
    # do same filename checks for checked files
    for variable, values in dd_dict.items():
        print("Verifying files in checked for:", variable)
        variable = variable
        datatype = values[0]
        allowed_suffixes = values[1].split(", ")
        fileexts = values[2].split(", ") # with or without . ?
        allowed_vals = values[3].split(", ")
        possible_exts = sum([ext.split('|') for ext in fileexts], [])
        numfiles = len(fileexts)

        if sessions:
            expected_sessions = []
            for ses in allowed_suffixes:
                ses_re = re.match("(s[0-9]+_r[0-9]+)(_e[0-9]+)?", ses)
                if ses_re:
                    expected_sessions.append(ses_re.group(1))
        else:
            expected_sessions = [""]
        for sub in listdir(checked):
            if sub.startswith("sub-"):
                for ses in expected_sessions:
                    if isdir(join(checked, sub, ses, datatype)):
                        # check that files in checked match conventions
                        path = join(checked, sub, ses, datatype)
                        corrected = False
                        for raw_file in listdir(path):
                            if re.match('^[Dd]eviation.*$', raw_file):
                                corrected = True
                                break
                        check_filenames(path, sub, ses, datatype, allowed_suffixes, possible_exts, numfiles, variable, corrected)
    print("Verifying numbers of files in subdirectories in checked")
    for sub in listdir(checked):
        if isdir(join(checked, sub)):
            for session_folder in listdir(join(checked, sub)):
                if isdir(join(checked, sub, session_folder)):
                    for datatype_folder in datatype_folders:
                        tasks = []
                        for task, vals in dd_dict.items():
                            if vals[0] == datatype_folder:
                                tasks.append(task)
                        path = join(checked, sub, session_folder, datatype_folder)
                        if isdir(path):
                            corrected = False
                            for raw_file in listdir(path):
                                if re.match('^[Dd]eviation.*$', raw_file):
                                    corrected = True
                                    break
                            check_number_of_files(path, datatype_folder, tasks, corrected)
