from colorama import Fore, Style


class ResultLogger:
    def __init__(self, output_file: str) -> None:
        self.output_file = output_file

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
        with open(self.output_file, "a") as file:
            file.write(f"{text}\n")
