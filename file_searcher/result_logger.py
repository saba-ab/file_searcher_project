from colorama import Fore, Style
from pathlib import Path


class ResultLogger:
    def __init__(self, output_folder: str) -> None:
        self.output_folder = output_folder

    def log_success(self, message: str) -> None:
        print(Fore.GREEN + message + Style.RESET_ALL)

    def log_error(self, message: str) -> None:
        print(Fore.RED + message + Style.RESET_ALL)

    def log_info(self, message: str) -> None:
        print(Fore.YELLOW + message + Style.BRIGHT)

    def write_to_file(self, text: str) -> None:
        """
        Write results to the specified output file.
        """
        with open(f"{self.output_folder}/results.txt", "a") as file:
            file.write(f"{text}\n")

        file.close()

    def write_passwords_to_file(self, file_path: Path) -> None:
        """
        write passwords into passwords.txt file
        """
        with open(file_path, 'r') as password_storage:
            content = password_storage.read()
            with open(f"{self.output_folder}/passwords.txt", "a") as file:
                file.write(f"{content}\n")

            file.close()
        password_storage.close()
        self.log_success(
            f"Password has successfully written in {self.output_folder}/passwords.txt")
