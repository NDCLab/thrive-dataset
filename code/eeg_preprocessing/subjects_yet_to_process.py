#!/usr/bin/env python3

import sys
import pandas as pd
import math

if __name__ == "__main__":
    dataset = sys.argv[1]
    session = sys.argv[2]

    central_tracker = "/home/data/NDClab/datasets/" + dataset + "/data-monitoring/central-tracker_" + dataset + ".csv"
    tracker_df = pd.read_csv(central_tracker, index_col = "id")
    datadict_df = pd.read_csv("/home/data/NDClab/datasets/" + dataset + "/data-monitoring/data-dictionary/central-tracker_datadict.csv")

    # get task names
    tasks = []
    for _, row in datadict_df.iterrows():
        if row["dataType"] == "eeg":
            tasks.append(row["variable"])

    all_ids = tracker_df.index.tolist()
    #processed_ids = tracker_df.index[tracker_df["eeg_preprocessed_" + session] == 1].tolist()
    #processed_ids = tracker_df.index[tracker_df["plangbbs_" + session + "_e1"] == 1].tolist()
    #processed_ids = tracker_df.index[tracker_df["all_eeg_preprocessing_" + session + "_e1_complete"] == 2].tolist()
    processed_ids = tracker_df.index[tracker_df[tasks[0] + "_preprocessing_" + session + "_e1_complete"] == 2].tolist() #TODO work for multiple eeg tasks
    unprocessed_ids = list(set(all_ids).difference(set(processed_ids)))
    unprocessed_ids = [str(x) for x in unprocessed_ids]

    #print(",".join(unprocessed_ids))
    print("/".join(unprocessed_ids))
