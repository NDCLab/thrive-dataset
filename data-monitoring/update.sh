#!/bin/bash

DATASET="/home/data/NDClab/datasets/thrive-dataset"

# ensure we have the latest version of hallMonitor 2.0
cd /home/data/NDClab/tools/lab-devOps/ || exit
git checkout data-monitoring-v2.0 || exit && git pull
rm -rf "$DATASET/data-monitoring/hallMonitor2/"
cp -r scripts/monitor/hallMonitor2 "$DATASET/data-monitoring/"
git checkout main
