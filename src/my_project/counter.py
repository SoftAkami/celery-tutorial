import sys
import logging

import time
from datetime import datetime


def custom_counter(t: int):
    logging.info("Counter root logger")
    logging.getLogger('my_project').info("Counter project logger")
    print(f"Running my counter", file=sys.stdout)
    for i in range(t):
        print(i)
        logging.getLogger("my_project").info(i)
        time.sleep(10)
    return datetime.now()