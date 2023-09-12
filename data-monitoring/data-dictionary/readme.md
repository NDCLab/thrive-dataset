# Datadict Column Definitions

The columns below are expected in the central tracker datadict:

* **variable**: exact name of data variable
* **datatype**: type of data; e.g., consent, psychopy, eeg, digi, audio, video, redcap_data, redcap_scrd, or other data type
* **description**: human-readable description of the variable
* **detail**: clarification of how the variable value is calculated/derived
* **allowedSuffix**: sX_rX_eX, where s=session, r=run, and e=event; separated by commas
* **measureUnit**: indication of the computer-readable value type used for the variable (i.e., Integer, Real, Logical, Char, Time)
* **allowedValues**: all allowed values for the variable, separated by commas: Integers and Real numbers as [x,y] (with integer sets separated by commas); Logical as 0, 1; Likert/Categorical as 1, 2, 3; Char as "text"
* **valueInfo**: indication of the meanings of the allowed values; categorical-type options may be separated by \| (vertical bar) or ; (semicolon)
* **naValueType**: indication of how NA values are flagged (NA, NaN, etc.)
* **activeStatus**: indication of whether variable is currently being used/collected
* **replacement**: for inactive variables, indication of any variable that was used in replacement
* **provenance**: indication of whether variable is collected directly from the participant and by what platform (direct-redcap, direct-psychopy, direct-pavlovia) or, if not direct, the origin of its derivation (that is, the script the calculates it, specified as code-SCRIPT, such as code-instruments or code-preproc.R, or the protocol used for manual coding, such as manual-errorCoding)
* **expectedFileExt**: the file extensions expected for each data type, separated by commas (e.g., ".eeg, .vmrk, .vhdr" for EEG data); if multiple extensions are allowed but not necessarily all expected, extensions can be separated by "\|" (e.g., ".zip.gpg \| .tar.gz.gpg")
