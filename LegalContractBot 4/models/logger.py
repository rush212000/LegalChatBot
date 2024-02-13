# logger.py

import logging
from logging.handlers import RotatingFileHandler
import os

# Configuration for the logger
LOG_FILE = 'LegalContractBot.log'
LOG_LEVEL = logging.INFO  # Could be changed to DEBUG, WARNING, etc., as needed
MAX_LOG_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
BACKUP_COUNT = 5  # Keep five old log files

# Create a logger
logger = logging.getLogger('LegalContractBot')
logger.setLevel(LOG_LEVEL)

# Create a file handler which logs even debug messages
if not os.path.exists('logs'):
    os.makedirs('logs')
fh = RotatingFileHandler(os.path.join('logs', LOG_FILE), maxBytes=MAX_LOG_FILE_SIZE, backupCount=BACKUP_COUNT)
fh.setLevel(LOG_LEVEL)

# Create a console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)  # Only log errors and critical messages to the console

# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

def log_debug(message):
    logger.debug(message)

def log_info(message):
    logger.info(message)

def log_warning(message):
    logger.warning(message)

def log_error(message):
    logger.error(message)

def log_critical(message):
    logger.critical(message)
