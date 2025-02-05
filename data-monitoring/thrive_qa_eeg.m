%clear all;
%clc;

% to Run on FIU HPC
% create a local cluster object
cluster = parcluster('local');

% start matlabpool with max workers set in the slurm file
parpool(cluster, str2num(getenv('SLURM_CPUS_PER_TASK'))) % this should be same as --cpus-per-task

% temp test code; remove
pool = gcp('nocreate');  % Get the current parallel pool without creating a new one
if isempty(pool)
    disp('No parallel pool is currently running.');
else
    disp(['Parallel pool with ', num2str(pool.NumWorkers), ' workers is running.']);
end

addpath(genpath('/home/data/NDClab/tools/lab-devOps/scripts/MADE_pipeline_standard/eeg_preprocessing'));% enter the path of the folder in this line
addpath(genpath('/home/data/NDClab/tools/lab-devOps/scripts/MADE_pipeline_standard/eeglab13_4_4b')); % enter the path of the EEGLAB folder in this line
rmpath(['/home/data/NDClab/tools/lab-devOps/scripts/MADE_pipeline_standard/eeglab13_4_4b' filesep 'functions' filesep 'octavefunc' filesep 'signal']);

% Define the dataset path and session
r_name = 'Felix';
dtype = 'eeg';
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

fname_filler = '';

% Open a log file for writing
csv_log = table('Size', [length(subject_data_paths), 8], ...
                'VariableTypes', {'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string'}, ...
                'VariableNames', {'name', 'date', 'sub', 'session', 'dtype', 'fname', 'status', 'notes'});

% Initialize all status values to empty string
csv_log.name(:) = '';
csv_log.date(:) = '';
csv_log.sub(:) = '';
csv_log.session(:) = '';
csv_log.dtype(:) = '';
csv_log.fname(:) = '';
csv_log.status(:) = '';
csv_log.notes(:) = '';

% Create temporary variables for parfor
r_name_array = strings(length(subject_data_paths), 1);
date_array = strings(length(subject_data_paths), 1);
sub_array = strings(length(subject_data_paths), 1);
session_array = strings(length(subject_data_paths), 1);
dtype_array = strings(length(subject_data_paths), 1);
fname_array = strings(length(subject_data_paths), 1);
status_array = strings(length(subject_data_paths), 1);
notes_array = strings(length(subject_data_paths), 1);


datetime_str = datestr(now, 'yyyy_mm_dd_HH_MM_SS');
csv_file = sprintf('qa_log_eeg_%s_%s.csv', session, datetime_str);
dfile = sprintf('qa_log_eeg_%s_%s.txt', session, datetime_str);
diary(dfile);

% Loop through each subject data path
parfor i = 1:length(subject_data_paths)
    all_stim = 0;
    all_resp = 0;
    stimuli = 0;
    responses = 0;
    sub_path = subject_data_paths{i};
    disp(sub_path);
    deviation = 0;
    fprintf('\n');

    % Extract the subject ID using the pattern
    sub = regexp(sub_path, pattern, 'tokens');
    sub = sub{1}{1};
    r_name_array(i) = r_name;
    date_array(i) = datestr(now, 'yyyy-mm-dd');
    sub_array(i) = sub;
    session_array(i) = session;
    dtype_array(i) = dtype;
    %fname_array(i) = '';
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
        for j = 1:length(extensions)
            found_extensions(extensions{j}) = false;
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
                    %[~] = evalc('EEG = pop_loadbv(eeg_files(1).folder, eeg_files(1).name)');
                    EEG = pop_loadbv(eeg_files(1).folder, eeg_files(1).name);
                    EEG = eeg_checkset(EEG);
                    [EEG, selected_events] = pop_selectevent(EEG, 'type', stim_events);
                    if length(selected_events) >= stim_count_thresh
                        stimuli = 1;
                    elseif length(selected_events) >= some_trial_count & length(selected_events) < stim_count_thresh
                        if ~deviation
                            fprintf('sub-%s has SOME stimulus events and no deviation was found! FAILED!\n', sub);
                            status_array(i) = 'FAILED';
                            notes_array(i) = 'NO/NOT ENOUGH EVENTS';
                        elseif deviation
                            fprintf('sub-%s has deviation and SOME stimulus events! FAILED!\n', sub);
                            status_array(i) = 'FAILED';
                            notes_array(i) = 'NO/NOT ENOUGH EVENTS';
                        end
                    else  
                        if ~deviation
                            fprintf('sub-%s has NO stimulus events and no deviation was found! FAILED!\n', sub);
                            status_array(i) = 'FAILED';
                            notes_array(i) = 'NO/NOT ENOUGH EVENTS';
                        elseif deviation
                            fprintf('sub-%s has deviation and NO stimulus events! FAILED!\n', sub);
                            status_array(i) = 'FAILED';
                            notes_array(i) = 'NO/NOT ENOUGH EVENTS';
                        end
                    end
                    [EEG, selected_events] = pop_selectevent(EEG, 'type', resp_events);
                    if length(selected_events) >= resp_count_thresh
                        responses = 1;
                    elseif length(selected_events) >= some_trial_count & length(selected_events) < resp_count_thresh
                        if ~deviation
                            fprintf('sub-%s has SOME response events and no deviation was found! FAILED!\n', sub);
                            status_array(i) = 'FAILED';
                            notes_array(i) = 'NO/NOT ENOUGH EVENTS';
                        elseif deviation
                            fprintf('sub-%s has deviation and SOME response events! FAILED!\n', sub);
                            status_array(i) = 'FAILED';
                            notes_array(i) = 'NO/NOT ENOUGH EVENTS';
                        end
                    else
                        if ~deviation
                            fprintf('sub-%s has NO response events and no deviation was found! FAILED!\n', sub);
                            status_array(i) = 'FAILED';
                            notes_array(i) = 'NO/NOT ENOUGH EVENTS';
                        elseif deviation
                            fprintf('sub-%s has deviation and NO response events! FAILED!\n', sub);
                            status_array(i) = 'FAILED';
                            notes_array(i) = 'NO/NOT ENOUGH EVENTS';
                        end
                    end
                catch ME
                    fprintf('sub-%s FAILED to load! FAILED!\nError message: %s', sub, ME.message);
                    status_array(i) = 'FAILED';
                    notes_array(i) = 'FAILS TO LOAD';
                end
            end
        end
    elseif length(sub_eeg_files) ~= 3
        sub_stim_count = 0;
        sub_resp_count = 0;
        if ~deviation
            fprintf('sub-%s has incorrect number of files and no deviation was found! FAILED!\n', sub);
            status_array(i) = 'FAILED';
            notes_array(i) = 'INCORRECT FILES/EXTENSIONS';
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
                   status_array(i) = 'FAILED';
                   notes_array(i) = 'FAILS TO LOAD';
                end
            end
            if sub_stim_count >= stim_count_thresh
                all_stim = 1;
                fprintf('sub-%s has deviation but ALL stimulus events!\n', sub);
            elseif sub_stim_count >= some_trial_count & sub_stim_count < stim_count_thresh
                all_stim = 0;
                fprintf('sub-%s has deviation and SOME stimulus events! FAILED!\n', sub);
                status_array(i) = 'FAILED';
                notes_array(i) = 'NO/NOT ENOUGH EVENTS';
            else    
                fprintf('sub-%s has deviation and NO stimulus events! FAILED!\n', sub);
                all_stim = 0;
                status_array(i) = 'FAILED';
                notes_array(i) = 'NO/NOT ENOUGH EVENTS';
            end
            if sub_resp_count >= resp_count_thresh
                all_resp = 1;
                fprintf('sub-%s has deviation but ALL response events!\n', sub);
            elseif sub_resp_count >= some_trial_count & sub_resp_count < resp_count_thresh
                all_resp = 0;
                fprintf('sub-%s has deviation and SOME response events! FAILED!\n', sub);
                status_array(i) = 'FAILED';
                notes_array(i) = 'NO/NOT ENOUGH EVENTS';
            else    
                all_resp = 0;
                fprintf('sub-%s has deviation and NO response events! FAILED!\n', sub);
                status_array(i) = 'FAILED';
                notes_array(i) = 'NO/NOT ENOUGH EVENTS';
            end
        end
    end
    if stimuli == 1 & responses == 1
        fprintf('sub-%s has ALL events! PASSED!\n', sub);
        status_array(i) = 'PASSED';
    elseif all_stim == 1 & all_resp == 1
        fprintf('sub-%s has ALL events! PASSED!\n', sub);
        status_array(i) = 'PASSED';
    else
        fprintf('sub-%s does NOT have all events! FAILED!\n', sub);
        status_array(i) = 'FAILED';
        notes_array(i) = 'NO/NOT ENOUGH EVENTS';
    end
end  
csv_log.name(:) = r_name_array;
csv_log.date(:) = date_array;
csv_log.sub(:) = sub_array;
csv_log.session(:) = session_array;
csv_log.dtype(:) = dtype_array;
csv_log.fname(:) = fname_array;
csv_log.status(:) = status_array;
csv_log.notes(:) = notes_array;           
writetable(csv_log, csv_file, 'WriteRowNames', true);
diary off

