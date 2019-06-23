# The program's "main menu", handling and passing variables to whichever mode is requested.

## Import Functions ---------------------------------------------------------- ##
from gmail_api import gmail_send
from X0_administrative import logger, status
from X3_responses_greetings_farewells import check_if_greeting_request, greeting_response
from X3_responses_coach import check_if_coach_request, coach_response
from X3_responses_wallet import check_if_wallet_request, wallet_response


## Request|Reply Functions ---------------------------------------------------------- ##
# Categorizes & replies to the request

# Main Function
def fulfill_request(reply_user, request_content):
    status.session_state = True
    # GREETING
    if check_if_greeting_request(request_content) == True:
        # Sets user status variables
        status.last_call = 'greeting'
        reply_messages = greeting_response()
    # COACH
    elif check_if_coach_request(request_content) == True:
        # Sets user status variables
        status.last_call = 'coach'
        reply_messages = coach_response(request_content)
    # WALLET
    elif check_if_wallet_request(request_content) == True:
        # Sets user status variables
        status.last_call = 'wallet'
        reply_messages = wallet_response(request_content)
    # Could not categorize request
    else:
        reply_messages = ["Request could not be categorized."]
        logger.warning(reply_messages)
        # Sets user status variables
        status.last_call = 'greeting'
    return reply_and_log(reply_user, reply_messages)

## reply_and_log ---------------------------------------------------------- ##
def reply_and_log(reply_user, reply_messages):
    for reply_message in reply_messages:
        response_confirmation = gmail_send(reply_user, reply_message)
        if response_confirmation == True:
            logger.info("Response Sent")
        else:
            logger.error("Response Failed to Send")
    return
