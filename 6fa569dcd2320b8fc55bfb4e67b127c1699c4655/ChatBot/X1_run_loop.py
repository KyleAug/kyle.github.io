# Defines the loop that the ChatBot program runs and its updating frequency.

## Imported Modules ---------------------------------------------------------- ##
import time
from X0_administrative import logger, status, sleep_timer
from gmail_api import gmail_read
from X2_start_action_thread import initiate_action

## Run Loop ---------------------------------------------------------- ##

while True:
    # Check for emails
    reply_user, request = gmail_read()
    if request != False:
        # If there is an unread email, creates a new worker to fulfill the request:
        logger.debug(str(request)+" from "+str(reply_user))
        initiate_action(reply_user, request)
    else: logger.info("No New Messages")
    # Sleeps at least 2 seconds before the next check
    time.sleep(2)
    sleep_timer(status.session_state)
    # Restarts the loop
    logger.debug("Finished sleeping... Currently restarting the loop.")
