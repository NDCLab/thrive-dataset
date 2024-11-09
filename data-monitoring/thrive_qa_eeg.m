%clear all;
%clc;


% to Run on FIU HPC%
% create a local cluster object
%cluster = parcluster('local');

% start matlabpool with max workers set in the slurm file
%parpool(cluster, str2num(getenv('SLURM_CPUS_PER_TASK'))) % this should be same as --cpus-per-task

%temp test code; remove
%pool = gcp('nocreate');  % Get the current parallel pool without creating a new one
%if isempty(pool)
%    disp('No parallel pool is currently running.');
%else
%    disp(['Parallel pool with ', num2str(pool.NumWorkers), ' workers is running.']);
%end
addpath(genpath('/home/data/NDClab/tools/lab-devOps/scripts/MADE_pipeline_standard/eeg_preprocessing'));% enter the path of the folder in this line
addpath(genpath('/home/data/NDClab/tools/lab-devOps/scripts/MADE_pipeline_standard/eeglab13_4_4b')); % enter the path of the EEGLAB folder in this line
rmpath(['/home/data/NDClab/tools/lab-devOps/scripts/MADE_pipeline_standard/eeglab13_4_4b' filesep 'functions' filesep 'octavefunc' filesep 'signal']);

% Define the dataset path and session
dataset_path = '/home/data/NDClab/datasets/thrive-dataset/sourcedata/checked/'; % Modify if your behavioral data is in another folder
session = 's1_r1'; % Modify if using for another session
% Get the list of subject data paths
subject_data_paths = dir(fullfile(dataset_path, 'sub-*/', session));
to_remove = ismember({subject_data_paths.name}, {'.', '..','.DS_Store'});
subject_data_paths = subject_data_paths(~to_remove);
subject_data_paths = {subject_data_paths.folder};
subject_data_paths = sort(subject_data_paths);
subject_data_paths = unique(subject_data_paths);

% Define the pattern to extract the subject ID
pattern = 'sub-(\d{7})';

% Define the extensions to check for
extensions = {'.eeg', '.vhdr', '.vmrk'};
stim_events = {'S 41', 'S 42', 'S 43', 'S 44', 'S 51', 'S 52', 'S 53', 'S 54'};
stim_count_thresh = 800;
resp_events = {'S 11', 'S 12', 'S 21', 'S 22'};
resp_count_thresh = 500;

some_trial_count = 100;

% Open a log file for writing
dfile = sprintf('qa_log_eeg_%s.txt', datestr(now, 'yyyy-mm-dd_HH-MM-SS'));
diary(dfile);

% Loop through each subject data path
for i = 1:length(subject_data_paths)
    stimuli = 0;
    responses = 0;
    sub_path = subject_data_paths{i};
    disp(sub_path);
    deviation = 0;
    fprintf('\n');

    % Extract the subject ID using the pattern
    sub = regexp(sub_path, pattern, 'tokens');
    sub = sub{1}{1};

    % Define the subject folder path
    subject_folder = fullfile(dataset_path, sprintf('sub-%s/%s/eeg/', sub, session));

    % Get the list of psychopy files in the subject folder
    sub_eeg_files = dir(fullfile(subject_folder, '*'));
    sub_eeg_files = {sub_eeg_files.name};
    sub_eeg_files = sub_eeg_files(~ismember(sub_eeg_files, {'.', '..','.DS_Store'}));
    sub_eeg_files = sort(sub_eeg_files);

    % Check if a deviation.txt file is present in the subject folder
    if any(strcmp('deviation.txt', sub_eeg_files))
        deviation = 1;
    end
    if length(sub_eeg_files) == 3
        % Initialize found_extensions with False values
        found_extensions = containers.Map('KeyType', 'char', 'ValueType', 'logical');
        for ext = extensions
            found_extensions(ext{1}) = false;
        end

        % Check file extensions
        for k = 1:length(sub_eeg_files)
            [~, ~, ext] = fileparts(sub_eeg_files{k});
            if found_extensions.isKey(ext)
                found_extensions(ext) = true;
            end
        end

        % Check if all 3 extensions are found
        if sum(cell2mat(found_extensions.values)) == 3
            % Read EEG file
            eeg_files = dir(fullfile(subject_folder, '*.vhdr'));
            disp(eeg_files)
            if ~isempty(eeg_files)
                try
                    EEG = pop_loadbv(eeg_files(1).folder, eeg_files(1).name);
                    EEG = eeg_checkset(EEG);
                    [EEG, selected_events] = pop_selectevent(EEG, 'type', stim_events);
                    if length(selected_events) >= stim_count_thresh
                        stimuli = 1;
                    elseif length(selected_events) >= some_trial_count & length(selected_events) < stim_count_thresh
                        fprintf('sub-%s has SOME stimulus events! FAILED!\n', sub);
                    else    
                        fprintf('sub-%s has NO stimulus events! FAILED!\n', sub);
                    end
                    [EEG, selected_events] = pop_selectevent(EEG, 'type', resp_events);
                    if length(selected_events) >= resp_count_thresh
                        responses = 1;
                    elseif length(selected_events) >= some_trial_count & length(selected_events) < resp_count_thresh
                        fprintf('sub-%s has SOME response events! FAILED!\n', sub);
                    else    
                        fprintf('sub-%s has NO response events! FAILED!\n', sub);
                    end
                catch ME
                    fprintf('sub-%s FAILED to load! FAILED!\nError message: %s', sub, ME.message);
                end
            end
        end
    elseif length(sub_eeg_files) ~= 3
        sub_stim_count = 0;
        sub_resp_count = 0;
        if ~deviation
            fprintf('sub-%s has incorrect number of files and no deviation was found! FAILED!\n', sub);
        elseif deviation
            eeg_files = dir(fullfile(subject_folder, '*.vhdr'));
            for l = 1:length(eeg_files)
                try
                    EEG = pop_loadbv(eeg_files(l).folder, eeg_files(l).name);
                    EEG = eeg_checkset(EEG);
                    [EEG, selected_events] = pop_selectevent(EEG, 'type', stim_events);
                    sub_stim_count = sub_stim_count + length(selected_events);
                    [EEG, selected_events] = pop_selectevent(EEG, 'type', resp_events);
                    sub_resp_count = sub_resp_count + length(selected_events);
                catch ME
                   fprintf('sub-%s FAILED to load! FAILED!\nError message: %s', sub, ME.message);
                end
            end
            if sub_stim_count >= stim_count_thresh
                fprintf('sub-%s has deviation but ALL stimulus events! PASSED!\n', sub);
            elseif sub_stim_count >= some_trial_count & sub_stim_count < stim_count_thresh
                fprintf('sub-%s has deviation and SOME stimulus events! FAILED!\n', sub);
            else    
                fprintf('sub-%s has deviation and NO stimulus events! FAILED!\n', sub);
            end
            if sub_resp_count >= resp_count_thresh
                fprintf('sub-%s has deviation but ALL response events! PASSED!\n', sub);
            elseif sub_resp_count >= some_trial_count & sub_resp_count < resp_count_thresh
                fprintf('sub-%s has deviation and SOME response events! FAILED!\n', sub);
            else    
                fprintf('sub-%s has deviation and NO response events! FAILED!\n', sub);
            end
        end
    end
    if stimuli == 1 & responses == 1
        fprintf('sub-%s has ALL events! PASSED!\n', sub);
    end
end             

diary off
