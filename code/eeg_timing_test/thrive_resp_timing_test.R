

#######  www.ndclab.com   ###########
# By: Kianoosh Hosseini at NDCLab@FIU  
# This script reads text files that include triggers sent to the recorder laptop.
# This script is changed for different timing tests.
# These files have ".vmrk" extension.
# install.packages("pracma")
library(stringr)
library(pracma)
library(dplyr)

#setwd("~/Users/kihossei/Desktop") #set working directory to where your text file (the one that you have triggers and their times) is located.
path <- ("/Users/kihossei/Documents/GitHub/thrive-dataset/code/eeg_timing_test")

mrkTxt <- readLines(paste(path, "/sys_1_timetest_resp.vmrk", sep = "")) # load the .vmrk file into the workspace.
myDat <- setNames(data.frame(matrix(nrow = length(mrkTxt), ncol = 1)), c("colA")) # creates an empty data frame with a single column and row # = length(mrkTxt)

# This for loop creates a dataframe from the loaded text file. 
for (i in 1:length(mrkTxt)) {
  myDat[i, 1] <- mrkTxt[i]
  
}

# Keep rows that have the string "Stimulus"
newDat <- myDat %>%
  filter(
    str_detect(colA, "Stimulus")
  )
# Let's delete all the strings to "Stimulus,"
for (i in 1:nrow(newDat)) {
  newDat$colB[i] <- gsub(".*Stimulus,", "", newDat$colA[i]) 
}

# Let's delete all the strings after the ms of the sent marker!
for (i in 1:nrow(newDat)) {
  newDat$colC[i] <- gsub(",1,0*.", "", newDat$colB[i]) 
}

newDat <- subset(newDat, select = -c(colA, colB)) # removing the colA and colB columns.
proc_fileName <- "resp_timing_output.csv"
write.csv(newDat,paste(path,proc_fileName, sep = "/", collapse = NULL), row.names=FALSE)

newDat <- read.csv(paste(path,proc_fileName, sep = "/", collapse = NULL))

timeVal <- setNames(data.frame(matrix(ncol = 1)), c("timeDiff")) # creating an empty data frame that will be filled with time difference values!
dVal <- setNames(data.frame(matrix(ncol = 1)), c("timeDiff"))

# If you wana perform the flanker timing test for responses run the code below!
# Stim trak markers come first and then resp triggers appear! They may be sent at the same time. In this case, they sum up.
# For ex., 128 (stim trak marker) adds to 11 or 12 (resp triggers) and become either S139 or S140!
main_dat <- setNames(data.frame(matrix(ncol = 5)), c("condition_type", "trial_num", "stim_marker_sent", "marker_sent", "time_sent")) # an empty data frame that will store these information.
# in the loop below, we find stim markers and then use "while" loop to find all the markers sent during that trial.
# markers sent 2000 ms after the stim marker are not included in that trial.
# The same trial number and "stim_marker_sent" are used for the markers sent in a given trial.
trial_num_counter <- 1

for (i in 1:nrow(newDat)){
  if (str_detect(newDat$colC[i], "S 41")  || str_detect(newDat$colC[i], "S 42") || str_detect(newDat$colC[i], "S 43") || str_detect(newDat$colC[i], "S 44")){ # detects non-social stim markers
    current_trial_num <- trial_num_counter # store the current trial number so, we can use it below
    trial_num_counter <- trial_num_counter + 1 # as we have found the stim marker above, we update trial number counter for the next trial
    stim_marker_sent <- gsub(",.*", "", newDat$colC[i]) # The stim marker was sent
    condition_type <- "non_social"
    trial_num <- current_trial_num
    marker_sent <- stim_marker_sent # The stim marker was sent
    time_sent <- str2num(gsub(".*,", "", newDat$colC[i])) # the time when the stim marker was sent
    main_dat[nrow(main_dat) + 1,] <- c(condition_type, trial_num, stim_marker_sent, marker_sent, time_sent)

    n <- 1 # counter for the while loop below
    if ((i + n) <= nrow(newDat)){
      while (!str_detect(newDat$colC[i + n], "S 41")  && !str_detect(newDat$colC[i + n], "S 42") && !str_detect(newDat$colC[i + n], "S 43") && !str_detect(newDat$colC[i + n], "S 44") && !str_detect(newDat$colC[i + n], "S 51")  && !str_detect(newDat$colC[i + n], "S 52") && !str_detect(newDat$colC[i + n], "S 53") && !str_detect(newDat$colC[i + n], "S 54") && !str_detect(newDat$colC[i + n], "S  1")  && !str_detect(newDat$colC[i + n], "S  2") && !str_detect(newDat$colC[i + n], "S  3") && !str_detect(newDat$colC[i + n], "S  4")){
        current_marker_sent_time <- str2num(gsub(".*,", "", newDat$colC[i + n]))
        stim_marker_sent_time <- str2num(gsub(".*,", "", newDat$colC[i]))
        time_diff_checker <- current_marker_sent_time - stim_marker_sent_time # to make sure this marker is within this trial
        if (time_diff_checker < 2000){ # checking to see if the following marker was sent in this trial
          stim_marker_sent <- gsub(",.*", "", newDat$colC[i]) # the stim marker sent in this trial
          condition_type <- "non_social"
          trial_num <- current_trial_num
          marker_sent <- gsub(",.*", "", newDat$colC[i + n]) # the marker sent
          time_sent <- str2num(gsub(".*,", "", newDat$colC[i + n])) # the time when the marker was sent
          main_dat[nrow(main_dat) + 1,] <- c(condition_type, trial_num, stim_marker_sent, marker_sent, time_sent)
        }
      }
      n <- n + 1 # updating the counter for "while" loop
    }
  } else if (str_detect(newDat$colC[i], "S 51")  || str_detect(newDat$colC[i], "S 52") || str_detect(newDat$colC[i], "S 53") || str_detect(newDat$colC[i], "S 54")){ # detects social stim markers
    current_trial_num <- trial_num_counter
    trial_num_counter <- trial_num_counter + 1
    stim_marker_sent <- gsub(",.*", "", newDat$colC[i]) # the stim marker sent in this trial
    condition_type <- "social"
    trial_num <- current_trial_num
    marker_sent <- stim_marker_sent # the stim marker sent in this trial
    time_sent <- str2num(gsub(".*,", "", newDat$colC[i])) # the time when the stim marker was sent
    main_dat[nrow(main_dat) + 1,] <- c(condition_type, trial_num, stim_marker_sent, marker_sent, time_sent)

    n <- 1
    if ((i + n) <= nrow(newDat)){
      while (!str_detect(newDat$colC[i + n], "S 41")  && !str_detect(newDat$colC[i + n], "S 42") && !str_detect(newDat$colC[i + n], "S 43") && !str_detect(newDat$colC[i + n], "S 44") && !str_detect(newDat$colC[i + n], "S 51")  && !str_detect(newDat$colC[i + n], "S 52") && !str_detect(newDat$colC[i + n], "S 53") && !str_detect(newDat$colC[i + n], "S 54") && !str_detect(newDat$colC[i + n], "S  1")  && !str_detect(newDat$colC[i + n], "S  2") && !str_detect(newDat$colC[i + n], "S  3") && !str_detect(newDat$colC[i + n], "S  4")){
        current_marker_sent_time <- str2num(gsub(".*,", "", newDat$colC[i + n]))
        stim_marker_sent_time <- str2num(gsub(".*,", "", newDat$colC[i]))
        time_diff_checker <- current_marker_sent_time - stim_marker_sent_time # to make sure this marker is within this trial
        if (time_diff_checker < 2000){ # checking to see if the following marker was sent in this trial
          stim_marker_sent <- gsub(",.*", "", newDat$colC[i]) # the stim marker sent in this trial
          condition_type <- "social"
          trial_num <- current_trial_num
          marker_sent <- gsub(",.*", "", newDat$colC[i + n]) # the marker was sent
          time_sent <- str2num(gsub(".*,", "", newDat$colC[i + n])) # the time when the marker was sent
          main_dat[nrow(main_dat) + 1,] <- c(condition_type, trial_num, stim_marker_sent, marker_sent, time_sent)
        }
      }
      n <- n + 1 # updating the counter for "while" loop
    }

  } else if (str_detect(newDat$colC[i], "S  1")  || str_detect(newDat$colC[i], "S  2") || str_detect(newDat$colC[i], "S  3") || str_detect(newDat$colC[i], "S  4")){ # detects practice stim markers
    current_trial_num <- trial_num_counter
    trial_num_counter <- trial_num_counter + 1
    stim_marker_sent <- gsub(",.*", "", newDat$colC[i]) # the stim marker sent in this trial
    condition_type <- "practice"
    trial_num <- current_trial_num
    marker_sent <- stim_marker_sent # the stim marker sent in this trial
    time_sent <- str2num(gsub(".*,", "", newDat$colC[i])) # the time when the stim marker was sent
    main_dat[nrow(main_dat) + 1,] <- c(condition_type, trial_num, stim_marker_sent, marker_sent, time_sent)
    n <- 1
    if ((i + n) <= nrow(newDat)){
      while (!str_detect(newDat$colC[i + n], "S 41")  && !str_detect(newDat$colC[i + n], "S 42") && !str_detect(newDat$colC[i + n], "S 43") && !str_detect(newDat$colC[i + n], "S 44") && !str_detect(newDat$colC[i + n], "S 51")  && !str_detect(newDat$colC[i + n], "S 52") && !str_detect(newDat$colC[i + n], "S 53") && !str_detect(newDat$colC[i + n], "S 54") && !str_detect(newDat$colC[i + n], "S  1")  && !str_detect(newDat$colC[i + n], "S  2") && !str_detect(newDat$colC[i + n], "S  3") && !str_detect(newDat$colC[i + n], "S  4")){
        current_marker_sent_time <- str2num(gsub(".*,", "", newDat$colC[i + n]))
        stim_marker_sent_time <- str2num(gsub(".*,", "", newDat$colC[i]))
        time_diff_checker <- current_marker_sent_time - stim_marker_sent_time # to make sure this marker is within this trial
        if (time_diff_checker < 2000){ # checking to see if the following marker was sent in this trial
          stim_marker_sent <- gsub(",.*", "", newDat$colC[i]) # the stim marker sent in this trial
          condition_type <- "practice"
          trial_num <- current_trial_num
          marker_sent <- gsub(",.*", "", newDat$colC[i + n]) # the marker was sent
          time_sent <- str2num(gsub(".*,", "", newDat$colC[i + n])) # the time when the marker was sent
          main_dat[nrow(main_dat) + 1,] <- c(condition_type, trial_num, stim_marker_sent, marker_sent, time_sent)
        }
      }
      n <- n + 1 # updating the counter for "while" loop
    }
  }
}
#
# Computing the response time offset using the data set created above (i.e., main_dat)
latency_dat <- setNames(data.frame(matrix(ncol = 4)), c("condition_type", "trial_num", "stim_marker_sent", "time_diff")) # an empty dataframe that will be filled with this information.
number_of_trials <- max(as.numeric(main_dat$trial_num), na.rm = TRUE) # total number of trials in this dataset (i.e., main_dat)

for (trial_num_in_dat in 1:number_of_trials){
  epoch_dat <- filter(main_dat, trial_num == trial_num_in_dat) # epoching each trial that will be used below to compute the response time offset
  temp_time_from_epoch_dat <- setNames(data.frame(matrix(ncol = 1)), c("timeDiff")) # an empty data frame


  for (i in 1:nrow(epoch_dat)) {
    if (str_detect(epoch_dat$marker_sent[i], "S139") || str_detect(epoch_dat$marker_sent[i], "S140") || str_detect(epoch_dat$marker_sent[i], "S149") || str_detect(epoch_dat$marker_sent[i], "S150") ||  str_detect(epoch_dat$marker_sent[i], "S128")) {
      if (str_detect(epoch_dat$marker_sent[i], "S139") || str_detect(epoch_dat$marker_sent[i], "S140") || str_detect(epoch_dat$marker_sent[i], "S149") || str_detect(epoch_dat$marker_sent[i], "S150")){
        if (str_detect(epoch_dat$marker_sent[i-1], "S128")){
          task_sent_mrk <- as.numeric(epoch_dat$time_sent[i])
          stimTrak_mrk <- as.numeric(epoch_dat$time_sent[i-1])
          timeDiff <- task_sent_mrk - stimTrak_mrk # stim trak trigger came first and then the marker from laptop
          temp_time_from_epoch_dat [nrow(temp_time_from_epoch_dat) + 1,] <- c(timeDiff)

        } else if (str_detect(epoch_dat$marker_sent[i-1], "S 11") || str_detect(epoch_dat$marker_sent[i-1], "S 12") || str_detect(epoch_dat$marker_sent[i-1], "S 21") || str_detect(epoch_dat$marker_sent[i-1], "S 22")){
          stimTrak_mrk <- as.numeric(epoch_dat$time_sent[i])
          task_sent_mrk <- as.numeric(epoch_dat$time_sent[i-1])
          timeDiff <- task_sent_mrk - stimTrak_mrk # The marker from laptop (task sent trigger) came first and then the stim trak trigger!
          temp_time_from_epoch_dat [nrow(temp_time_from_epoch_dat) + 1,] <- c(timeDiff)
        } else {
          task_sent_mrk <- as.numeric(epoch_dat$time_sent[i])
          stimTrak_mrk <- task_sent_mrk
          timeDiff <- task_sent_mrk - stimTrak_mrk # both sent at the same time!
          temp_time_from_epoch_dat [nrow(temp_time_from_epoch_dat) + 1,] <- c(timeDiff)
        }
      } else if (str_detect(epoch_dat$marker_sent[i], "S128")) {
        if (str_detect(epoch_dat$marker_sent[i-1], "S 11") || str_detect(epoch_dat$marker_sent[i-1], "S 12") || str_detect(epoch_dat$marker_sent[i-1], "S 21") || str_detect(epoch_dat$marker_sent[i-1], "S 22")){
          stimTrak_mrk <- as.numeric(epoch_dat$time_sent[i])
          task_sent_mrk <- as.numeric(epoch_dat$time_sent[i-1])
          timeDiff <- task_sent_mrk - stimTrak_mrk # The marker from laptop (task sent trigger) came first and then the stim trak trigger!
          temp_time_from_epoch_dat [nrow(temp_time_from_epoch_dat) + 1,] <- c(timeDiff)
        }
      } else { # in case of having NA in this row
        next
      }
    } else { # in case of no response in this trial
      next
    }
  }
  temp_time_from_epoch_dat <- na.omit(temp_time_from_epoch_dat) # removing NA rows
  condition_type <- epoch_dat$condition_type[1]
  trial_num <- epoch_dat$trial_num[1]
  stim_marker_sent <- epoch_dat$stim_marker_sent[1]
  if (nrow(temp_time_from_epoch_dat) != 0){
    for (xx in 1:nrow(temp_time_from_epoch_dat)){ # this loop is for cases when there are more than one responses and time offset values in a given trial. So, it does include all time offsets.
      time_diff <- as.numeric(temp_time_from_epoch_dat$timeDiff[xx])
      latency_dat[nrow(latency_dat) + 1,] <- c(condition_type, trial_num, stim_marker_sent, time_diff)
    }
  } else if (nrow(temp_time_from_epoch_dat) == 0){
    time_diff <- NA
    latency_dat[nrow(latency_dat) + 1,] <- c(condition_type, trial_num, stim_marker_sent, time_diff)
  }
}
latency_dat$time_diff <- as.numeric(latency_dat$time_diff)
# min(latency_dat$time_diff, na.rm = TRUE)
# max(latency_dat$time_diff, na.rm = TRUE)
mean(latency_dat$time_diff, na.rm = TRUE)
sd(latency_dat$time_diff, na.rm = TRUE)

reorderd_latency_dat_max_to_min <- latency_dat %>% arrange(desc(time_diff)) # reordering data set for visual inspection


<<<<<<< Updated upstream:code/eeg_timing_test/mini_mfe_resp_timing_test.R
######## Below is the timing test results for the Flanker task of the thrive study task on April 5, 2023- System 2 with block level trigger loss ######
# response triggers
# mean(test$value)
# 1.700855
# sd(test$value)
# 2.085521
=======
>>>>>>> Stashed changes:code/eeg_timing_test/thrive_resp_timing_test.R








