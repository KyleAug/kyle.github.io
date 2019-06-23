# The support that creates a thread to execute a specific request.

## Import Modules ---------------------------------------------------------- ##

import threading
from X0_administrative import logger, status
from X2_main_menu import fulfill_request
from X3_responses_greetings_farewells import check_if_end_session_request

## Request|Reply Functions
# 1. Starts a new thread for each request
# 2. Defines the threads
# 3. reply_and_log


## Main Function ---------------------------------------------------------- ##
# Starts a new thread for each request
def initiate_action(reply_user, requests):
    if requests != False:
        for individual_request in requests:
            # Initiate Response
            if check_if_end_session_request(individual_request) == False:
                # convert session_state to True
                status.session_state = True
                # starts a new thread to fulfill the request
                Initiate_Response(reply_user, individual_request).start()
            # End Session Request
            else:
                # Converts status to default
                status.session_state = False
                status.last_call = False
                status.tag = 0
    else:
        logger.info("No actions required")
    return

## Defines the threads ---------------------------------------------------------- ##
class Initiate_Response(threading.Thread):
   def __init__(self, reply_user, request_content):
      threading.Thread.__init__(self)
      self.reply_user = reply_user
      self.request_content = request_content
   def run(self):
       #Write your execution code here
       logger.debug("Initiated Response: "+str(self.request_content))
       fulfill_request(self.reply_user, self.request_content)
       # update_request_type(modified_request_type)
       return
