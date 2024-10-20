import pytest
from file_searcher.file_searcher import FileSearcher
from file_searcher.result_logger import ResultLogger
from pathlib import Path
from unittest.mock import MagicMock


def test_search_finds_passwords_txt(tmp_path):
    logger = MagicMock(ResultLogger)
    searcher = FileSearcher(logger)

    test_file = tmp_path / "passwords.txt"
    test_file.write_text("This is a test passwords file.")

    searcher.search(tmp_path)

    logger.log_success.assert_called_with(f"Found: {test_file}")
    logger.write_to_file.assert_called_with(test_file)


def test_search_ignores_other_files(tmp_path):
    logger = MagicMock(ResultLogger)
    searcher = FileSearcher(logger)

    test_file = tmp_path / "otherFile.txt"
    test_file.write_text("This is not the file you were expecting.")

    searcher.search(tmp_path)

    logger.log_success.assert_not_called()
    logger.write_to_file.assert_not_called()
