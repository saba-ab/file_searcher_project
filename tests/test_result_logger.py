import pytest
from file_searcher.result_logger import ResultLogger
from unittest.mock import MagicMock


def test_log_success(capsys):
    logger = ResultLogger("results.txt")

    logger.log_success("Test success message")

    captured = capsys.readouterr()

    assert "Test success message" in captured.out


def test_write_to_file(tmp_path):
    test_file = tmp_path / "results.txt"

    logger = ResultLogger(test_file)

    logger.write_to_file("Test file output")

    assert test_file.read_text() == "Test file output\n"
