import datetime
import os
import re

import pandas as pd
import pytest
import pytz
from mock import Mock

from hallmonitor.tests.integration.base_cases import (
    ExpectedError,
    TestCase,
    ValidationTestCase,
)

TZ_INFO = pytz.timezone("US/Eastern")


class MiscellaneousTestCase(ValidationTestCase):
    pass


class BaseTestCase(MiscellaneousTestCase):
    """
    Test case for no modifications to the base subject data.
    """

    case_name = "BaseTestCase"
    description = "Copies the base subject data exactly."
    conditions = ["No variations to base subject data"]
    expected_output = "No errors are raised."

    @property
    def behavior_to_test(self) -> str:
        return "Tests to make sure no errors are raised for unaltered data."

    def modify(self, base_files):
        return base_files.copy()

    def get_expected_errors(self):
        return []


def test_base(request):
    BaseTestCase.run_test_case(request)


class InsufficientFilesTestCase(MiscellaneousTestCase):
    """
    Test case for incorrect number of files in a folder (not enough).
    """

    case_name = "InsufficientFilesTestCase"
    description = "Deletes a file from a folder that should contain multiple files."
    conditions = ["Folder contains fewer files than expected"]
    expected_output = "Error is raised for insufficient number of files in folder."

    def modify(self, base_files):
        modified_files = base_files.copy()
        target_file = f"sub-{self.sub_id}_arrow-alert-v1-1_psychopy_s1_r1_e1.csv"

        if not self.remove_file(modified_files, target_file):
            raise FileNotFoundError(f"File matching basename {target_file} not found")

        return modified_files

    def get_expected_errors(self):
        basename = f"sub-{self.sub_id}_arrow-alert-v1-1_psychopy_s1_r1_e1.csv"
        missing_info = f"Expected file {basename} not found"
        errors = [ExpectedError("Missing file", re.escape(missing_info))]

        return errors


def test_insufficient_files(request):
    InsufficientFilesTestCase.run_test_case(request)


class ExtraFilesInFolderTestCase(MiscellaneousTestCase):
    """
    Test case for incorrect number of files in a folder (extra files present).
    """

    case_name = "ExtraFilesInFolderTestCase"
    description = (
        "Adds an additional file to the folder so it has more files than expected."
    )
    conditions = [
        "Folder contains more files than expected",
    ]
    expected_output = "Error is raised for folder containing extra files."

    def modify(self, base_files):
        modified_files = base_files.copy()

        original_suffix = "s1_r1_e1"
        new_suffix = "s1_r1_e2"

        base_file = f"sub-{self.sub_id}_arrow-alert-v1-1_psychopy_{original_suffix}.csv"
        base_file = self.build_path("s1_r1", "psychopy", base_file)
        additional_file = base_file.replace(original_suffix, new_suffix)

        # copy original file contents
        modified_files[additional_file] = modified_files[base_file]

        return modified_files

    def get_expected_errors(self):
        naming_info = r"Suffix s1_r1_e2 not in allowed suffixes.*"
        unexpected_info = f"Unexpected file sub-{self.sub_id}_arrow-alert-v1-1_psychopy_s1_r1_e2.csv found"
        errors = [
            ExpectedError("Naming error", naming_info),
            ExpectedError("Unexpected file", re.escape(unexpected_info)),
        ]

        return errors


def test_extra_files_in_folder(request):
    ExtraFilesInFolderTestCase.run_test_case(request)


class EmptyFileTestCase(MiscellaneousTestCase):
    """
    Test case for correctly named files that are empty.
    """

    case_name = "EmptyFileTestCase"
    description = "Creates an empty (0 bytes) file, retaining its correct name."
    conditions = [
        "File is named correctly",
        "File is empty (0 bytes)",
    ]
    expected_output = (
        "Error is raised for file that is correctly named but contains no data."
    )

    def modify(self, base_files):
        modified_files = base_files.copy()

        target = f"sub-{self.sub_id}_arrow-alert-v1-1_psychopy_s1_r1_e1.csv"
        target = self.build_path("s1_r1", "psychopy", target)

        if target not in modified_files:
            raise FileNotFoundError(f"File matching relative path {target} not found")

        # simulate empty file (0 bytes)
        modified_files[target] = ""

        return modified_files

    def get_expected_errors(self):
        basename = f"sub-{self.sub_id}_arrow-alert-v1-1_psychopy_s1_r1_e1.csv"
        info_regex = r"(?:.*/)+" + re.escape(basename)

        errors = [
            ExpectedError("Empty file", f"Found empty file {info_regex}"),
            ExpectedError("Psychopy error", f"No data found in {info_regex}"),
        ]

        return errors


def test_empty_file(request):
    EmptyFileTestCase.run_test_case(request)


class ExpectedFileMissingTestCase(MiscellaneousTestCase):
    """
    Test case for missing expected files based on the data dictionary.
    """

    case_name = "ExpectedFileMissingTestCase"
    description = (
        "Deletes a file that is expected to be present based on the data dictionary."
    )
    conditions = [
        "File expected based on data dictionary is missing",
    ]
    expected_output = "Error is raised for missing expected file."

    def modify(self, base_files):
        modified_files = base_files.copy()
        target_file = f"sub-{self.sub_id}_arrow-alert-v1-1_psychopy_s1_r1_e1.csv"

        if not self.remove_file(modified_files, target_file):
            raise FileNotFoundError(f"File matching basename {target_file} not found")

        return modified_files

    def get_expected_errors(self):
        basename = f"sub-{self.sub_id}_arrow-alert-v1-1_psychopy_s1_r1_e1.csv"
        missing_info = re.escape(f"Expected file {basename} not found")

        errors = [
            ExpectedError("Missing file", missing_info),
        ]

        return errors


def test_expected_file_missing(request):
    ExpectedFileMissingTestCase.run_test_case(request)


class MultipleTasksFromCombinationRowTestCase(MiscellaneousTestCase):
    """
    Test case for the presence of multiple tasks from the same combination row.
    """

    case_name = "MultipleTasksFromCombinationRowTestCase"
    description = "Duplicates a file from a task in a combination row and renames it to appear as another task from the same row."
    conditions = ["Folder contains multiple tasks from the same combination row"]
    expected_output = (
        "Error is raised for multiple tasks present in the same combination row."
    )

    def modify(self, base_files):
        modified_files = base_files.copy()

        template = f"sub-{self.sub_id}_VARNAME_s1_r1_e1.csv"
        template = self.build_path("s1_r1", "psychopy", template)
        existing_file = template.replace("VARNAME", "arrow-alert-v1-1_psychopy")
        duplicate_file = template.replace("VARNAME", "arrow-alert-v1-2_psychopy")

        if existing_file not in modified_files:
            raise FileNotFoundError(f"File matching basename {existing_file} not found")

        modified_files[duplicate_file] = modified_files[existing_file]

        return modified_files

    def get_expected_errors(self):
        basename_v1_1 = f"sub-{self.sub_id}_arrow-alert-v1-1_psychopy_s1_r1_e1"
        basename_v1_2 = f"sub-{self.sub_id}_arrow-alert-v1-2_psychopy_s1_r1_e1"
        ext_re = r"\..+"
        combination_info = "Multiple variables present for combination row arrow-alert_psychopy, expected one."
        missing_info = f"Expected file {basename_v1_2 + ext_re} not found"

        errors = [
            ExpectedError("Combination variable error", re.escape(combination_info), 2),
            ExpectedError("Missing file", missing_info, 2),
            ExpectedError(  # unexpected from the v1-2 identifier's "perspective"
                "Unexpected file", f"Unexpected file {basename_v1_1 + ext_re} found", 3
            ),
            ExpectedError(  # unexpected for the v1-1 identifier
                "Unexpected file", f"Unexpected file {basename_v1_2 + ext_re} found", 1
            ),
        ]

        return errors


def test_multiple_tasks_from_combination_row(request):
    MultipleTasksFromCombinationRowTestCase.run_test_case(request)


class DataDictionaryHasChangesTestCase(TestCase):
    case_name = "DataDictionaryHasChangesTestCase"
    description = "Modifies the data dictionary to simulate unexpected changes."
    behavior_to_test = (
        "Validation should raise an error if the data dictionary has been modified."
    )
    conditions = [
        "Data dictionary contents differ from the expected format or version."
    ]
    expected_output = "Error is raised indicating that the data dictionary has changed."

    def modify(self, base_files):
        modified_files = base_files.copy()

        datadict_path = os.path.join(
            "data-monitoring",
            "data-dictionary",
            "central-tracker_datadict.csv",
        )

        if datadict_path not in modified_files:
            raise FileNotFoundError(f"Could not find datadict at {datadict_path}")

        curr_content = modified_files[datadict_path]
        new_content = curr_content.replace("Participant ID", "participant ID")
        modified_files[datadict_path] = new_content

        return modified_files

    def validate(self):
        from hallmonitor.hallmonitor import main

        with pytest.raises(ValueError, match="Data dictionary has changed"):
            args = self.get_standard_args()
            main(args)


def test_data_dictionary_has_changes(request):
    DataDictionaryHasChangesTestCase.run_test_case(request)


class PendingFilesCsvCreatedTestCase(TestCase):
    """
    Test case to ensure that new pending-files and pending-errors CSVs are created
    by raw data validation if not already present.
    """

    case_name = "PendingFilesCsvCreatedTestCase"
    description = "Deletes pending CSVs to ensure new ones are created by the program."
    behavior_to_test = "Two new CSVs (pending-files and pending-errors) are created."
    conditions = [
        "pending-files and pending-errors CSVs are removed, simulating a first run."
    ]
    expected_output = (
        "CSVs with the names pending-files and pending-errors are created. These files' names should "
        "contain an appropriate matching timestamp and the files should have all expected columns."
    )

    def modify(self, base_files):
        modified_files = base_files.copy()

        # remove our pending CSVs
        modified_files = {
            relpath: contents
            for relpath, contents in modified_files.items()
            if not relpath.startswith("data-monitoring/pending/pending-")
        }

        # add back an empty directory
        pending_dir = os.path.join("data-monitoring", "pending", "")
        modified_files[pending_dir] = ""

        return modified_files

    def validate(self):
        # Raw data validation deals with pending-files and pending-errors,
        # while checked data validation only uses pending-errors. In this
        # test case, we want to examine the program's behavior for both.
        from hallmonitor.hallmonitor import raw_data_validation

        # save start time for later
        start_dt = datetime.datetime.now(tz=TZ_INFO)
        # remove sub-minute precision (seconds and microseconds)
        start_dt = start_dt.replace(second=0, microsecond=0)

        logger = Mock()  # no need to examine output
        raw_data_validation(
            logger,
            dataset=self.case_dir,
            use_legacy_exceptions=False,
        )

        pending_dir = os.path.join(self.case_dir, "data-monitoring", "pending")

        assert os.path.exists(pending_dir)
        assert os.path.isdir(pending_dir)

        pending_contents = os.listdir(pending_dir)
        assert len(pending_contents) == 2

        pending_file_name = [
            file
            for file in pending_contents
            if re.fullmatch(r"pending-files-\d{4}-\d{2}-\d{2}_\d{2}-\d{2}\.csv", file)
        ][0]
        file_df = pd.read_csv(os.path.join(pending_dir, pending_file_name))
        assert set(file_df.columns) == {
            "datetime",
            "user",
            "passRaw",
            "identifier",
            "subject",
            "dataType",
            "encrypted",
            "suffix",
            "errorType",
            "errorDetails",
        }

        pending_error_name = [
            file
            for file in pending_contents
            if re.fullmatch(r"pending-errors-\d{4}-\d{2}-\d{2}_\d{2}-\d{2}\.csv", file)
        ][0]
        error_df = pd.read_csv(os.path.join(pending_dir, pending_error_name))
        assert set(error_df.columns) == {
            "datetime",
            "user",
            "identifier",
            "subject",
            "dataType",
            "encrypted",
            "suffix",
            "errorType",
            "errorDetails",
        }

        # ensure timestamps match between the two files
        pending_files_ts = re.search(
            r"\d{4}-\d{2}-\d{2}_\d{2}-\d{2}", pending_file_name
        )
        pending_errors_ts = re.search(
            r"\d{4}-\d{2}-\d{2}_\d{2}-\d{2}", pending_error_name
        )
        assert pending_files_ts is not None
        pending_files_ts = pending_files_ts.group(0)

        assert pending_errors_ts is not None
        pending_errors_ts = pending_errors_ts.group(0)

        assert pending_files_ts == pending_errors_ts


def test_pending_files_csv_created(request):
    PendingFilesCsvCreatedTestCase.run_test_case(request)


class MissingTaskFromDataDictionaryTestCase(MiscellaneousTestCase):
    case_name = "MissingTaskFromDataDictionaryTestCase"
    description = (
        "Ensures that a missing task specified in a '_status' variable raises an error."
    )
    conditions = ["Removed file specified in the bbs_status variable."]
    expected_output = "An error is raised for the missing file."

    def modify(self, base_files):
        modified_files = base_files.copy()

        filename = f"sub-{self.sub_id}_arrow-alert-v1-1_psychopy_s1_r1_e1.csv"

        for _ in range(2):  # once for raw, once for checked
            if not self.remove_file(modified_files, filename):
                raise FileNotFoundError(f"File with basename {filename} not found")

        return modified_files

    def get_expected_errors(self):
        error_info = r"Expected file .+\.csv not found"
        errors = [ExpectedError("Missing file", info_regex=error_info)]

        return errors


def test_missing_task_from_data_dictionary(request):
    MissingTaskFromDataDictionaryTestCase.run_test_case(request)


class IgnoreBeforeDateTestCase(MiscellaneousTestCase):
    case_name = "IgnoreBeforeDateTestCase"
    description = "Sets an ignore date in the future."
    conditions = ["File with error has a date before the ignore date."]
    expected_output = "Error is not raised for file with date before ignore date."

    def modify(self, base_files):
        modified_files = base_files.copy()

        target = f"sub-{self.sub_id}_arrow-alert-v1-1_psychopy_s1_r1_e1.csv"
        target = self.build_path("s1_r1", "psychopy", target)

        if target not in modified_files:
            raise FileNotFoundError(f"File matching relative path {target} not found")

        # simulate empty file (0 bytes)
        modified_files[target] = ""

        return modified_files

    def get_expected_errors(self):
        # file with error is ignored due to date of last modification
        return []

    def validate(self):
        ignore_before_date = datetime.datetime.now() + datetime.timedelta(days=1)
        error_df = self.run_validate_data(ignore_before_date=ignore_before_date)
        self.compare_errors(error_df)


def test_ignore_before_date(request):
    IgnoreBeforeDateTestCase.run_test_case(request)


class DeleteFailedCheckedIdentifierTestCase(TestCase):
    case_name = "DeleteFailedCheckedIdentifierTestCase"
    description = "Deletes files for an identifier that failed checked data validation."
    conditions = ["Identifier has failed checked data validation"]
    behavior_to_test = "Ensures that files for identifiers failing checked data validation are removed."
    expected_output = (
        "All files related to the failed identifier are successfully deleted."
    )

    def modify(self, base_files):
        modified_files = base_files.copy()

        target = f"sub-{self.sub_id}_arrow-alert-v1-1_psychopy_s1_r1_e1.csv"
        target = self.build_path("s1_r1", "psychopy", target)

        if target not in modified_files:
            raise FileNotFoundError(f"File matching relative path {target} not found")

        # simulate empty file (0 bytes)
        modified_files[target] = ""

        return modified_files

    def validate(self):
        from hallmonitor import hallmonitor

        try:
            hallmonitor.checked_data_validation(logger=Mock(), dataset=self.case_dir)
        except Exception as err:
            raise AssertionError from err

        filepaths = self.get_paths(self.case_dir)

        # check that all files associated with the identifier were deleted from checked/
        id_checked_dir = self.build_path("s1_r1", "psychopy", "")
        assert not any(str(path).startswith(id_checked_dir) for path in filepaths)

        # check that the identifier's files in raw/ were not deleted
        id_raw_dir = self.build_path("s1_r1", "psychopy", "", True)
        assert any(str(path).startswith(id_raw_dir) for path in filepaths)


def test_delete_failed_checked_identifier(request):
    DeleteFailedCheckedIdentifierTestCase.run_test_case(request)


class KeepFailedIdentifierCheckedNoRawTestCase(TestCase):
    case_name = "KeepFailedIdentifierCheckedNoRawTestCase"
    description = (
        "Deletes raw files for an identifier that failed checked data validation."
    )
    conditions = ["Identifier has failed checked data validation"]
    expected_output = "No files related to the failed identifier are deleted."
    behavior_to_test = (
        "Ensures that checked files for identifiers failing checked "
        + "data validation and missing raw data are retained."
    )

    def modify(self, base_files):
        modified_files = base_files.copy()

        target = f"sub-{self.sub_id}_arrow-alert-v1-1_psychopy_s1_r1_e1.csv"
        target = self.build_path("s1_r1", "psychopy", target)

        if target not in modified_files:
            raise FileNotFoundError(f"File matching relative path {target} not found")

        # simulate empty file (0 bytes)
        modified_files[target] = ""

        # remove the identifier's files in the raw directory
        raw_dir = self.build_path("s1_r1", "psychopy", "", True)
        modified_files = {
            relpath: contents
            for relpath, contents in modified_files.items()
            if not relpath.startswith(raw_dir)
        }

        return modified_files

    def validate(self):
        from hallmonitor import hallmonitor

        try:
            hallmonitor.checked_data_validation(logger=Mock(), dataset=self.case_dir)
        except Exception as err:
            raise AssertionError from err

        filepaths = self.get_paths(self.case_dir)

        # check that the identifier's files in checked/ were not deleted
        id_checked_dir = self.build_path("s1_r1", "psychopy", "")
        assert any(str(path).startswith(id_checked_dir) for path in filepaths)

        # check that the identifier's files in raw/ were not restored
        id_raw_dir = self.build_path("s1_r1", "psychopy", "", True)
        assert not any(str(path).startswith(id_raw_dir) for path in filepaths)


def test_keep_failed_identifier_checked_no_raw(request):
    KeepFailedIdentifierCheckedNoRawTestCase.run_test_case(request)
