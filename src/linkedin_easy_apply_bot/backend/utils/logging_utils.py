import logging

from linkedin_easy_apply_bot.backend import config

logging.basicConfig(level=config.LOG_LEVEL)

def get_logger(name):
    return logging.getLogger(name)