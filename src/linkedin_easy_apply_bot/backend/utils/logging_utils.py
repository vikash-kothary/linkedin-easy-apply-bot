import logging

from linkedin_easy_apply_bot.backend import config

logging.basicConfig(level=config.LOG_LEVEL)

# Suppress selenium debug logs
logging.getLogger('selenium').setLevel(logging.INFO)

def get_logger(name):
    return logging.getLogger(name)
