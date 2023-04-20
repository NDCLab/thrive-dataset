# PsychoPy Experiments

### arrow_alert_v0

This is the main PsychoPy task that is run during data collection. It consists of a practice flanker task followed by three loops: two flanker tasks (social vs. non-social) and one observe-other condition. All conditions are counterbalanced, and counterbalance for a given participant is identified by the REDCap protocol. For more information on the data and variables from this task, please refer to the data dictionaries for this study.


### arrow-alert-v0-timingTest_block_level_triggerloss

This is a slightly modified version of the arrow_alert_v0 task. The only difference is that the target arrow size is increased by 10X. This modification allows us to perform timing tests. The block level refers to the fact that we resolve the issue of losing triggers (because of temporary disconnection of the USB ports from the stimuli computer to the trigger box) at the block level. So, when the connection is lost and triggers disappear, we only lose triggers for the current block of the flanker task. Triggers, then, re-appear in the following block. This block-level trigger loss fix is already applied to the main task. 

### arrow-alert-v0 -trial_level_triggerLoss

This is a version of the main task in which we were trying to fix trigger loss issue at the trial level. Due to time limitations, we paused on troubleshooting this version. So, for the THRIVE study, we fix trigger loss issue at the block level, as described above. 

### timestamp-v0

This is a simple task that shows X on the screen and simultaneously plays an audio sound. It enables us to use these visual and audio outputs in to synchronize timing during the social tasks across Zoom, Audacity, and EEG recordings.
