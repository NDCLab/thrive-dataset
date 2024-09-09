#!/bin/bash



#SBATCH --job-name=Kia_thrive_MADE         # create a short name for your job
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=1               # total number of tasks across all nodes
#SBATCH --cpus-per-task=4
#SBATCH --time=1000:00:00          # total run time limit (HH:MM:SS)
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-user=khoss005@fiu.edu

module load matlab-2021b
pwd; hostname; date


matlab -nodisplay < MADE_pipeline_v1_0_thrive_02.m