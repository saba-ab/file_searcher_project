import os
from pathlib import Path


class PathManager:

    @staticmethod
    def get_desktop_path() -> Path:
        """
        Get the Desktop path based to operating system.
        """
        if os.name == 'nt':
            print("Windows machine detected.")
            return Path.home() / "Desktop"
        else:
            print("UNIX machine detected.")
            return Path.home() / "Desktop"
