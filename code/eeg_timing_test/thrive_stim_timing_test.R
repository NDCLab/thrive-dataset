

#######  www.ndclab.com   ###########
# By: Kianoosh Hosseini at NDCLab@FIU  
# This script reads text files that include triggers sent to the recorder laptop.
# This script needed to be changed for different timing tests.
# These files have ".vmrk" extension.
# install.packages("pracma")
library(stringr)
library(pracma)
library(dplyr)

#setwd("~/Users/kihossei/Desktop") #set working directory to where your text file (the one that you have triggers and their times) is located.
path <- ("/Users/kihossei/Documents/GitHub/thrive-dataset/code/eeg_timing_test")

mrkTxt <- readLines(paste(path, "/thrive_sys1_timingTest_stim.vmrk", sep = "")) # load the .vmrk file into the workspace.
myDat <- setNames(data.frame(matrix(nrow = length(mrkTxt), ncol = 1)), c("colA")) # creates an empty data frame with a single column and row # = length(mrkTxt)

# This 'for' loop creates a dataframe from the loaded text file. 
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
proc_fileName <- "stim_timing_output.csv"
write.csv(newDat,paste(path,proc_fileName, sep = "/", collapse = NULL), row.names=FALSE)

newDat <- read.csv(paste(path,proc_fileName, sep = "/", collapse = NULL))

practice_dat <- setNames(data.frame(matrix(ncol = 1)), c("timeDiff")) # creating an empty data frame that will be filled with time difference values!
dVal <- setNames(data.frame(matrix(ncol = 1)), c("timeDiff"))

# If you wana perform the flanker timing test for stimulus presentation run the code below!
for (i in 1:nrow(newDat)) {
  if (str_detect(newDat$colC[i], "S128")) {
    if (i != 1){
      if ( str_detect(newDat$colC[i-1], "S  1")  || str_detect(newDat$colC[i-1], "S  2") || str_detect(newDat$colC[i-1], "S  3") || str_detect(newDat$colC[i-1], "S  4")){
        secondVal <- str2num(gsub(".*S128,", "", newDat$colC[i]))
        firstVal <- str2num(gsub(".*,", "", newDat$colC[i-1]))
        diffVal <- secondVal - firstVal
        dVal[1,] <- diffVal
        practice_dat <- rbind(practice_dat, dVal)
      }
    }
  } else {
    next
  }
}


practice_dat <- na.omit(practice_dat, na.action = "omit")
mean(practice_dat$timeDiff)
sd(practice_dat$timeDiff)


nonSocial_dat <- setNames(data.frame(matrix(ncol = 1)), c("timeDiff")) # creating an empty data frame that will be filled with time difference values!
dVal <- setNames(data.frame(matrix(ncol = 1)), c("timeDiff"))

# If you wana perform the flanker timing test for stimulus presentation run the code below!
for (i in 1:nrow(newDat)) {
  if (str_detect(newDat$colC[i], "S128")) {
    if (i != 1){
      if ( str_detect(newDat$colC[i-1], "S 41")  || str_detect(newDat$colC[i-1], "S 42") || str_detect(newDat$colC[i-1], "S 43") || str_detect(newDat$colC[i-1], "S 44")){
        secondVal <- str2num(gsub(".*S128,", "", newDat$colC[i]))
        firstVal <- str2num(gsub(".*,", "", newDat$colC[i-1]))
        diffVal <- secondVal - firstVal
        dVal[1,] <- diffVal
        nonSocial_dat <- rbind(nonSocial_dat, dVal)
      }
    }
  } else {
    next
  }
}
nonSocial_dat <- na.omit(nonSocial_dat, na.action = "omit")
mean(nonSocial_dat$timeDiff)
sd(nonSocial_dat$timeDiff)



social_dat <- setNames(data.frame(matrix(ncol = 1)), c("timeDiff")) # creating an empty data frame that will be filled with time difference values!
dVal <- setNames(data.frame(matrix(ncol = 1)), c("timeDiff"))

# If you wana perform the flanker timing test for stimulus presentation run the code below!
for (i in 1:nrow(newDat)) {
  if (str_detect(newDat$colC[i], "S128")) {
    if (i != 1){
      if ( str_detect(newDat$colC[i-1], "S 51")  || str_detect(newDat$colC[i-1], "S 52") || str_detect(newDat$colC[i-1], "S 53") || str_detect(newDat$colC[i-1], "S 54")){
        secondVal <- str2num(gsub(".*S128,", "", newDat$colC[i]))
        firstVal <- str2num(gsub(".*,", "", newDat$colC[i-1]))
        diffVal <- secondVal - firstVal
        dVal[1,] <- diffVal
        social_dat <- rbind(social_dat, dVal)
      }
    }
  } else {
    next
  }
}
social_dat <- na.omit(social_dat, na.action = "omit")
mean(social_dat$timeDiff)
sd(social_dat$timeDiff)

######## Below is the timing test results for the Flanker task of the thrive study task on March 31, 2023- Egret PC with the Old EEG equipment######
# stimulus triggers
# mean(test$value)
# 11.04167
#  sd(test$value)
#  1.657151


######## Below is the timing test results for the Flanker task of the thrive study task on March 31, 2023- Egret PC with the New EEG equipment######
# stimulus triggers
# mean(test$value)
# 11.475
#  sd(test$value)
# 1.534209


######## Below is the timing test results for the Flanker task of the thrive study task on April 5, 2023- System 2 with block level trigger loss ######
# stimulus triggers
# mean(test$value)
# 12
#  sd(test$value)
# 1.659059
######## Below is the timing test results for the Flanker task of the thrive study task on April 6, 2023- System 1 with block level trigger loss ######
# stimulus triggers
# mean(test$value)
# 11.46667
#  sd(test$value)
# 1.781951



######## Below is the timing test results for the Flanker task of the thrive study task on June 2, 2023- System 2
# stimulus triggers
# mean(test$value)
# 12.31915
#  sd(test$value)
# 1.575718
######## Below is the timing test results for the Flanker task of the thrive study task on April 2, 2023- System 1
# stimulus triggers
# mean(test$value)
# 12.775
#  sd(test$value)
# 1.576876







