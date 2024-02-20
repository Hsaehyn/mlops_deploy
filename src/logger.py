# the code for any application log
# track the activity happening inside the application

import logging
import os
from datetime import datetime

# Set Log File Name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_&S')}.log"
# Create Log Directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) # cwd: current working directory
# Set Log File Path 
# as other ppl may import the library, we need to set the Log File Path on their desktop
os.makedirs(logs_path, exist_ok=True) # "exist_ok=True" ensures that no error is raised if the directory already exist
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


# configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s -  %(levelname)s - %(message)s",
    # only log message witha  severity level of 'INFO' and above
    level = logging.INFO, 
)

# if __name__ == "__main__":
#     logging.info("Logging has started")


