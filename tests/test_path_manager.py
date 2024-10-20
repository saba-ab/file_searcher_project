import pytest
from file_searcher.path_manager import PathManager
from pathlib import Path
import os


def test_get_desktop_path_windows(monkeypatch):

    monkeypatch.setattr(Path, 'home', lambda: Path("C:/Users/TestUser"))

    desktop_path = PathManager.get_desktop_path()
    assert desktop_path == Path("C:/Users/TestUser/Desktop")


def test_get_desktop_path_unix(monkeypatch):
    monkeypatch.setattr(os, 'name', 'posix')
    monkeypatch.setattr(Path, 'home', lambda: Path("/home/testuser"))

    desktop_path = PathManager.get_desktop_path()
    assert desktop_path == Path("/home/testuser/Desktop")
