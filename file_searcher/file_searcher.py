from pathlib import Path
from .result_logger import ResultLogger


class FileSearcher:
    def __init__(self, logger: ResultLogger):
        self.logger = logger
        self.found_password = False

    def search(self, path: Path) -> None:
        """
        Search for files recursively within the given path and log results.
        """

        if self.found_password:
            return

        try:
            if path.is_dir():

                for file in path.iterdir():

                    if self.found_password:
                        return

                    if not file.is_dir():
                        self.logger.log_info(f"Not a match: {file}")
                        if file.name == "passwords.txt":
                            self.logger.log_success(f"Found: {file}")
                            self.logger.write_to_file(file)
                            self.found_password = True
                            return
                    else:
                        self.search(file)

        except PermissionError:
            self.logger.log_error(
                f"You don't have permission to access {path}")
        except OSError as e:
            self.logger.log_error(f"Error accessing {path}: {e}")
