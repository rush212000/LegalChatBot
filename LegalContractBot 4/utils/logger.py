import logging
import os
from logging.handlers import RotatingFileHandler

# Define the base directory for log files
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Log file configuration
LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Logger basic configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(module)s - %(funcName)s: %(message)s",
    handlers=[
        RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5),  # 1MB per file, keeping last 5 logs
        logging.StreamHandler()  # Print to stdout
    ]
)

# Export the logger
logger = logging.getLogger(__name__)

# Example usage
if __name__ == "__main__":
    logger.info("Logger initialized successfully.")
    logger.error("This is an error message for testing purposes.")
