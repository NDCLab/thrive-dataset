import sys
import os
import pandas as pd
from glob import glob
import re
from datetime import datetime

r_name = "Lilly"
dtype = "psychopy"
dataset_path = "/home/data/NDClab/datasets/thrive-dataset/sourcedata/checked/" # mofify if your behavioral data is in another folder
session = "s1_r1" # modify if using for another session
subject_data_paths = sorted(glob(f"{dataset_path}sub-*/{session}"))
pattern = r'sub-(\d{7})' # regex to take subject id
extensions = ['.log', '.csv', '.psydat']
n_blocks = 20
n_trials = 40
all_trial_count = n_blocks * n_trials
some_trial_count = 100

log_name = f"qa_logs/qa_log_behavior_{session}_{datetime.now().strftime('%d-%m-%Y_%H_%M_%S')}"
sys.stdout = open(f"{log_name}.txt", "wt") # write a log
csv_log = pd.DataFrame()
for row_num, path in enumerate(subject_data_paths):
    deviation = 0
    print("")
    sub = re.search(pattern, path).group(1)
    subject_folder = f"{dataset_path}sub-{sub}/{session}/psychopy/"
    sub_psychopy_files = sorted(glob(f"{subject_folder}*"))
    csv_log.loc[row_num, "name"] = r_name
    csv_log.loc[row_num, "date"] = datetime.now().strftime('%Y-%m-%d')
    csv_log.loc[row_num, "sub"] = sub
    csv_log.loc[row_num, "session"] = session
    csv_log.loc[row_num, "dtype"] = dtype
    csv_log.loc[row_num, "fname"] = ""

    if len(os.listdir(subject_folder)) > 0:
        if any(["no-data" in i for i in os.listdir(subject_folder)]): # first check if a deviation present
            no_data = 1
            print(f"sub-{sub} has NO DATA! FAILED!")
            csv_log.loc[row_num, "status"] = "FAILED"
            csv_log.loc[row_num, "notes"] = "NO DATA"
            continue
    if any(["deviation" in i for i in os.listdir(subject_folder)]): # first check if a deviation present
        deviation = 1

    sub_psychopy_output_files = [i.split("/")[-1] for i in sub_psychopy_files if (".csv" in i or ".psydat" in i or ".log" in i)]
    csv_log.loc[row_num, "fname"] = ",".join(sub_psychopy_output_files)    

    if len(sub_psychopy_files) == 3: # best case scenario if only 3 files are present
        found_extensions = {ext: False for ext in extensions}
        for psychopy_file in sub_psychopy_files:
            _, ext = os.path.splitext(psychopy_file)
            if ext in found_extensions:
                found_extensions[ext] = True
        if sum([item[1] for item in list(found_extensions.items())]) == 3: # ideal case, all 3 files are correct extension
            try:
                psychopy_data = pd.read_csv(glob(f"{subject_folder}*.csv")[0])
                start_index = psychopy_data.loc[:, "task_blockText.started"].first_valid_index()
                psychopy_data = psychopy_data.iloc[start_index:, :].dropna(subset = ["middleStim"])
                psychopy_data = psychopy_data[psychopy_data["conditionText"].isin(["Observed", "Alone"])].reset_index(drop=True) # check num of trials
                if psychopy_data.shape[0] == all_trial_count:
                    print(f"sub-{sub} has ALL trial data! PASSED!")
                    csv_log.loc[row_num, "status"] = "PASSED"
                elif psychopy_data.shape[0] < all_trial_count and psychopy_data.shape[0] > some_trial_count:
                    print(f"sub-{sub} has SOME trial data! FAILED!")
                    csv_log.loc[row_num, "status"] = "FAILED"
                    csv_log.loc[row_num, "notes"] = "NO/NOT ENOUGH TRIALS"
                else:
                    print(f"sub-{sub} has NO trial data! FAILED!")
                    csv_log.loc[row_num, "status"] = "FAILED"
                    csv_log.loc[row_num, "notes"] = "NO/NOT ENOUGH TRIALS"
            except:
                print(f"sub-{sub} file FAILS to load!")
                csv_log.loc[row_num, "status"] = "FAILED"
                csv_log.loc[row_num, "notes"] = "FAILS TO LOAD"
        else:
            print(f"sub-{sub} has 3 files BUT not with correct extensions! FAILED!")
            csv_log.loc[row_num, "status"] = "FAILED"
            csv_log.loc[row_num, "notes"] = "INCORRECT FILES/EXTENSIONS"
    elif len(sub_psychopy_files) != 3:
        sub_trial_count = 0
        if not deviation: # do not continue if not all files are correct AND no deviation
            print(f"sub-{sub} has incorrect number of files and no deviation was found! FAILED!")
            csv_log.loc[row_num, "status"] = "FAILED"
            csv_log.loc[row_num, "notes"] = "INCORRECT FILES/EXTENSIONS"
        elif deviation: # if deviation, try counting all trials from all csvs in the folder
            sub_csv_files = sorted(glob(f"{subject_folder}*.csv"))
            for csv_fname in sub_csv_files:
                try:
                    psychopy_data = pd.read_csv(csv_fname)
                    if "task_blockText.started" in list(psychopy_data.columns): # count trials from only task-related csv
                        start_index = psychopy_data.loc[:, "task_blockText.started"].first_valid_index()
                        psychopy_data = psychopy_data.iloc[start_index:, :].dropna(subset = ["middleStim"])
                        psychopy_data = psychopy_data[psychopy_data["conditionText"].isin(["Observed", "Alone"])].reset_index(drop=True) # check num of trials
                        sub_trial_count += psychopy_data.shape[0]
                    else:
                        pass # skip if not task-related csv
                except:
                    print(f"sub-{sub} has deviation and file FAILS to load!")
                    csv_log.loc[row_num, "status"] = "FAILED"
                    csv_log.loc[row_num, "notes"] = "FAILS TO LOAD"
            if sub_trial_count == all_trial_count:
                print(f"sub-{sub} has deviation but ALL trial data! PASSED!")
                csv_log.loc[row_num, "status"] = "PASSED"
            elif sub_trial_count < all_trial_count and sub_trial_count > some_trial_count:
                print(f"sub-{sub} has deviation and SOME trial data! FAILED!")
                csv_log.loc[row_num, "status"] = "FAILED"
                csv_log.loc[row_num, "notes"] = "NO/NOT ENOUGH TRIALS"
            else:
                print(f"sub-{sub} has deviation and NO trial data! FAILED!")
                csv_log.loc[row_num, "status"] = "FAILED"
                csv_log.loc[row_num, "notes"] = "NO/NOT ENOUGH TRIALS"
csv_log.to_csv(f"{log_name}.csv", index=False)
