from pathlib import Path
from .result_logger import ResultLogger


class FileSearcher:
    def __init__(self, logger: ResultLogger):
        self.logger = logger

    def search(self, path: Path) -> None:
        """
        Search for files recursively within the given path and log results.
        """
        try:
            if path.is_dir():

                for file in path.iterdir():
                    if not file.is_dir():
                        self.logger.log_info(f"Checking: {file}")
                        if file.name == "passwords.txt" or file.name == "Passwords.txt":
                            self.logger.log_success(f"Found: {file}")
                            self.logger.write_to_file(file)
                            self.logger.write_passwords_to_file(file)
                    else:
                        self.search(file)

        except PermissionError:
            self.logger.log_error(
                f"You don't have permission to access {path}")
        except OSError as e:
            self.logger.log_error(f"Error accessing {path}: {e}")
