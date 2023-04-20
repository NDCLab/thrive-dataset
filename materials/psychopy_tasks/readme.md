# Psychopy tasks

### Instructions

arrow_alert_v0: This is the main PsychoPy task that is run during data collection. It consists of a practice flanker task followed by three loops: two flanker tasks (social vs. non-social) and one observe other condition. All conditions are counterbalanced, and counterbalance for a given participant is identified by redcap. For more information on the data and variables from this task, please refer to the data dictionaries for this study.

arrow-alert-v0-timingTest_block_level_triggerloss: This is a slightly modified version of the arrow_alert_v0 task. The only difference is that the target arrow size is increased by 10X. This modification allows us to perform timing tests. The block level refers to the fact that we resolve the issue of losing triggers (because of temporary disconnection of the USB ports from the stimuli computer to the trigger box) at the block level. So, when the connection is lost and triggers disappear, we only lose triggers for the current block of the flanker task. Triggers, then, re-appear in the following block. This block level trigger loss fix is already applied to the main task. 

arrow-alert-v0 -trial_level_triggerLoss: This is the version of the main task with which we were trying to fix trigger loss issue at the trial level. As we had limited time, we had to pause troubleshooting this version. So, we fix trigger loss issue at the block level for the THRIVE study. 

timestamp-v0: this is the simple task that shows X on the screen and simultaneously plays an audio so that we can use both these visual and audio outputs in the Zoom, audacity, and EEG recordings to synchronize timings during the social tasks of the THRIVE study. 

### Project Notes
