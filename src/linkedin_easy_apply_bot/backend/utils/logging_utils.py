import os
import logging
from datetime import datetime, timedelta

from linkedin_easy_apply_bot.backend import config
from linkedin_easy_apply_bot.backend.utils import datetime_utils


# Suppress selenium debug logs
logging.getLogger("selenium").setLevel(logging.INFO)


def get_logger(name: str) -> logging.Logger:
    logs_dir = 'instances/logs'
    if not os.path.isdir(logs_dir):
        os.mkdir(logs_dir)

    # Logging defaults
    now: str = datetime_utils.to_datetime_string(datetime_utils.now())
    # TODO need to check if there is a log dir available or not
    log_file_name = f"{logs_dir}/{now}/applyJobs.log"
    logging.basicConfig(
        level=config.LOG_LEVEL,
        filename=log_file_name,
        filemode="w",
        format="%(asctime)s::%(name)s::%(levelname)s::%(message)s",
        datefmt=f"{logs_dir}/%d-%b-%y %H:%M:%S",
    )

    # Logging format
    log_format = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", "%H:%M:%S"
    )
    log_stream = logging.StreamHandler()
    log_stream.setLevel(logging.DEBUG)
    log_stream.setFormatter(log_format)

    # Logger
    logger = logging.getLogger(name) 
    logger.setLevel(logging.DEBUG)
    logger.addHandler(log_stream)
    return logger
