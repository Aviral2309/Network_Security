import logging
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

LOG_FORMAT = "[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)d] %(message)s"

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format=LOG_FORMAT,
    level=logging.INFO
)

logging.info("Logging initialized successfully")


'''
Let’s decode:

Token	Meaning
%(asctime)s	The date and time of the log event
%(lineo)d	❌ Typo — should be %(lineno)d (line number in code)
%(name)s	Name of the logger (often root if not customized)
%(levelname)s	Log level — e.g. INFO, WARNING, ERROR
%(message)s	The actual log message you log using logging.info() or logging.error()
'''