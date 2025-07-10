import os
import logging
from datetime import datetime, timedelta

from linkedin_easy_apply_bot.backend import config

# Suppress selenium debug logs
logging.getLogger("selenium").setLevel(logging.INFO)


def get_logger(name):
    log = logging.getLogger(name)
    dt: str = datetime.strftime(datetime.now(), "%m_%d_%y %H_%M_%S ")

    if not os.path.isdir("./logs"):
        os.mkdir("./logs")

    # TODO need to check if there is a log dir available or not
    logging.basicConfig(
        level=config.LOG_LEVEL,
        filename=("./logs/" + str(dt) + "applyJobs.log"),
        filemode="w",
        format="%(asctime)s::%(name)s::%(levelname)s::%(message)s",
        datefmt="./logs/%d-%b-%y %H:%M:%S",
    )
    log.setLevel(logging.DEBUG)
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.DEBUG)
    c_format = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", "%H:%M:%S"
    )
    c_handler.setFormatter(c_format)
    log.addHandler(c_handler)

    return log
