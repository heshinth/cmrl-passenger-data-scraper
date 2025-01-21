import logging
import os
from datetime import datetime


def setup_logger():
    # Create logs directory if it doesn't exist
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Create logger
    logger = logging.getLogger("cmrl_scraper")
    logger.setLevel(logging.INFO)

    # Create formatters
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_formatter = logging.Formatter("%(levelname)s: %(message)s")

    # File handler (logs to file)
    log_filename = f"logs/scraper_{datetime.now().strftime('%Y%m%d')}.log"
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(file_formatter)

    # Console handler (logs to console)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
