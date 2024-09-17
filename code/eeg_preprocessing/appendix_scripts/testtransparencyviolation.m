function EEG = edit_event_markers_thrive_copyy(EEG)
%
%%%%%% Label event markers%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% This script labels the thrive flanker task data. Labelling includes basic
% information about stimulus type and responses, as well as exhaustive 
% labeling of prior/next trial data.

%% debug code
% Kia commented debug code
%EEG = pop_loadbv('/Users/kihossei/OneDrive - Florida International University/Projects/sfe/scripts/sfe-dataset/sourcedata/raw/eeg', '160015_sfe_eeg_s1-r1-e1.vhdr');
%EEG = eeg_checkset(EEG);
%EEG = pop_resample( EEG, 250);
%EEG = eeg_checkset( EEG );
%for atm=1:length({EEG.event.type})
   % if isnumeric(EEG.event(atm).type)
      %  EEG.event(atm).type = num2str(EEG.event(atm).type);
  %  end
%end
%%

%% event codes from task

% %practice trials
% leftStim1             leftStim2        stimNum congruent target
% img/rightArrow.png	img/rightArrow.png	1       1       right
% img/leftArrow.png     img/leftArrow.png	2       1       left
% img/leftArrow.png     img/leftArrow.png	3       0       right
% img/rightArrow.png	img/rightArrow.png	4       0       left
% %nonsocial condition
% img/rightArrow.png	img/rightArrow.png	41      1       right
% img/leftArrow.png     img/leftArrow.png	42      1       left
% img/leftArrow.png     img/leftArrow.png	43      0       right
% img/rightArrow.png	img/rightArrow.png	44      0       left
% %social condition
% img/rightArrow.png	img/rightArrow.png	51      1       right
% img/leftArrow.png     img/leftArrow.png	52      1       left
% img/leftArrow.png     img/leftArrow.png	53      0       right
% img/rightArrow.png	img/rightArrow.png	54      0       left

%correct response: 11
%error response: 12
%technically correct response, but not the first response made: 21
%technically error response, but not the first response made: 22
    
%all stim and resp markers for the task
all_stimMarkers = {'S  1', 'S  2', 'S  3', 'S  4', 'S 41', 'S 42', 'S 43', ...
    'S 44', 'S 51', 'S 52', 'S 53', 'S 54'};
all_respMarkers = {'S 11', 'S 12', 'S 21', 'S 22'}; 

%subsets of stim/resp markers to be used in switch statements when
%labelling
practice_stimMarkers = {'S  1', 'S  2', 'S  3', 'S  4'};
mainTask_stimMarkers = {'S 41', 'S 42', 'S 43', 'S 44', 'S 51', 'S 52', 'S 53', 'S 54'};

ns_stimMarkers = {'S 41', 'S 42', 'S 43', 'S 44'};
s_stimMarkers = {'S 51', 'S 52', 'S 53', 'S 54'};

rightTarDir_stimMarkers = {'S  1', 'S  3', 'S 41', 'S 43', 'S 51', 'S 53'};
leftTarDir_stimMarkers = {'S  2', 'S  4', 'S 42', 'S 44', 'S 52', 'S 54'};

congruent_stimMarkers = {'S  1', 'S  2', 'S 41', 'S 42', 'S 51', 'S 52'};
incongruent_stimMarkers = {'S  3', 'S  4', 'S 43', 'S 44', 'S 53', 'S 54'};

first_RespMarkers = {'S 11', 'S 12'}; 
extra_RespMarkers = {'S 21', 'S 22'}; 

corr_RespMarkers = {'S 11'}; 
error_RespMarkers = {'S 12'}; 

%specify cutoff (in s) for how fast a valid rt can be
validRt_cutoff = .150;

EEG.event = 'event';
EEG.asdf = 'fdsa';

end
