# HallMonitor 2.0

The `hallmonitor` module is designed to ensure data integrity within the [NDCLab's](https://www.ndclab.com/) datasets. It validates files within raw and checked directories against a central tracker and data dictionary, performing checks for expected files, naming conventions, and handling exceptions such as `no-data.txt` and `deviation.txt` files. The module logs errors for missing, extra, or misnamed files, runs special checks for data types like EEG and Psychopy, and prepares valid files for QA.

## Features

- **Data Validation**: Validates the presence and correctness of files in raw and checked directories.
- **Error Logging**: Logs detailed information about missing, extra, or misnamed files.
- **Special Data Checks**: Performs specific checks for data types like EEG and Psychopy.
- **QA Preparation**: Prepares valid files for quality assurance checks.
- **Central Tracker Update**: Updates a central tracker with the status of validated files.

## Usage

To use the `hallmonitor` module, you need to ensure that the module is installed and accessible from your Python environment. You can achieve this by installing the module using `pip` and then running the script from any directory.

First, navigate to the root directory of the `hallmonitor` module and install it:

```sh
pip install .
```

After installation, you can run the `hallmonitor` script from any directory by using the following command:

```sh
python -m hallmonitor [dataset-path] [options]
```

### Options

- `-c, --child-data`: Indicates that the dataset includes child data.
- `-l, --legacy-exceptions`: Use legacy exception file behavior (deviation.txt and no-data.txt do not include identifier name).
- `-n, --no-color`: Disable color in output, useful for logging or plain-text environments.
- `--no-qa`: Skip the QA (quality assurance) step of the pipeline.
- `-o, --output`: Specify a file path for logger output (defaults to a timestamped file in data-monitoring/logs/).
- `--checked-only`: Only run data validation for data in sourcedata/checked/.
- `--raw-only`: Only run data validation for data in sourcedata/raw/.
- `-v, --verbose`: Print additional debugging information to the console.
- `-q, --quiet`: Do not print any information to the console.
- `-r, --replace`: Replace all REDCap columns with the passed values.
- `-m, --map`: Remap the names of specified REDCap columns.

## Example

To validate a dataset located at `/path/to/dataset` and log the output to a specific file, use:

```sh
python -m hallmonitor /path/to/dataset -o /path/to/logfile.log
```
