# main.py
import time
from file_searcher.file_searcher import FileSearcher
from file_searcher.result_logger import ResultLogger
from file_searcher.path_manager import PathManager


def main():
    start_time = time.time()

    logger = ResultLogger("tmp/results.txt")
    searcher = FileSearcher(logger)
    path_manager = PathManager()

    desktop_path = path_manager.get_desktop_path()

    searcher.search(desktop_path)

    elapsed_time = time.time() - start_time
    logger.log_success(f"Search completed in {elapsed_time:.2f} seconds.")


if __name__ == "__main__":
    main()
