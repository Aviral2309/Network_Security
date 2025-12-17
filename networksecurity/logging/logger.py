import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok = True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
  filename= LOG_FILE_PATH,
  format='[%(asctime)s] %(lineo)d %(name)s - %(levelname)s - %(message)s ',
  level = logging.INFO,
)

'''
Let’s decode:

Token	Meaning
%(asctime)s	The date and time of the log event
%(lineo)d	❌ Typo — should be %(lineno)d (line number in code)
%(name)s	Name of the logger (often root if not customized)
%(levelname)s	Log level — e.g. INFO, WARNING, ERROR
%(message)s	The actual log message you log using logging.info() or logging.error()
'''