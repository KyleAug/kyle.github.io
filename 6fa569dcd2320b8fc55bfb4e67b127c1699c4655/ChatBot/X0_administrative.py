

## Functions to Import -------------------------------------------------------------------- ##
# from administrative import logger, status, sleep_timer

# Example Call: print status.session_state

## Logging Functions -------------------------------------------------------------------- ##
import logging
logging.basicConfig(
    filename='chatbot_log.log',
    level=logging.DEBUG,
    format = '%(asctime)s -- %(threadName)s; %(filename)s; %(funcName)s; %(lineno)d; %(levelname)s -- %(message)s')
logger = logging.getLogger('chatbot_log.log')
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)
logging.getLogger('googleapiclient.discovery').setLevel(logging.WARNING)
# logger.info("hi")

## User_Status -------------------------------------------------------------------- ##
class User_Status():
    def __init__(self):
        # True or False
        self.session_state = False
        # False, 'coach', 'wallet'
        self.last_call = False
        # any integer
        self.tag = 0
        # 'key' is option_number: 'value' is the soup_id
        self.last_call_dict = {}

status = User_Status()

## Sleep Timer -------------------------------------------------------------------- ##
import time
def sleep_timer(session_state):
    if session_state == True:
        time.sleep(1)
    else:
        time.sleep(20)
    return
