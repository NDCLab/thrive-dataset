#!/usr/bin/env python3

import sys
from os import listdir, makedirs, system
from os.path import join, isdir, isfile, splitext

import shutil
import pandas as pd
import re
import math
import subprocess

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

def check_filenames(path, sub, ses, datatype, allowed_suffixes, possible_exts, numfiles):
        # check that files in raw and checked match conventions
        obs_files = []
        corrected = False
        for raw_file in listdir(path):
            if re.match('^[Dd]eviation.*$', raw_file):
                corrected = True
            else:
                obs_files.append(raw_file)
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
        if len(obs_files) > numfiles:
            print(c.RED + "Error: number of", datatype, "data files in subject folder", sub, str(len(obs_files)), "greater than the expected number", str(numfiles) + c.ENDC)
        elif len(obs_files) < numfiles:
            print(c.RED + "Error: number of", datatype, "data files in subject folder", sub, str(len(obs_files)), "less than the expected number", str(numfiles) + c.ENDC)
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
    for _, row in df_dd.iterrows():
        if not isinstance(row["expectedFileExt"], float):
            task_vars.append(row.name)

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
                    check_filenames(path, subject, ses, datatype, allowed_suffixes, possible_exts, numfiles)
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
                        check_filenames(path, sub, ses, datatype, allowed_suffixes, possible_exts, numfiles)
