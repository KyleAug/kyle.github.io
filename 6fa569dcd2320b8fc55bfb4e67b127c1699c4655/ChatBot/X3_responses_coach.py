# The file has two functions for the Coach mode:
    # Checks if Coach
        # Returns True or False
    # Creates a Response
        # Returns a response_text

## Imported Modules ---------------------------------------------------------- ##
from X0_administrative import logger, status
# To read
from X4_read_coach_content import understand_the_request, response_content_generator
# To update
from X4_update_coach_content import update_coach_content, coach_file

## Checks if Coach ---------------------------------------------------------- ##

def lower_case(content):
    return str(content).lower()
def initiate_coach_session():
    status.tag = 0
    return
coach_keywords = ['coach', 'content', 'help']

# Main Function
def check_if_coach_request(request_content):
    # If the user is currently in a coach session
    if status.last_call == 'coach':
        return True
    # If the user requests to start a coach session
    request_content = lower_case(request_content)
    for keyword in coach_keywords:
        if keyword in request_content:
            initiate_coach_session()
            return True
    else:
        return False

## Creates a Response ---------------------------------------------------------- ##

# Main Function
def coach_response(request_content):
    # Interprets the content of the request
    pass_fail, tag_one, tag_one_id, tag_two = understand_the_request(request_content)
    # Formulates a response message
    if pass_fail == True:
        response_messages = response_content_generator(tag_one, tag_one_id, tag_two)
        status.tag = int(tag_two[1])
    # If it cannot understand the request, returns an error message
    else:
        response_messages = ["Request could not be understood. Please try again."]
    # Returns a list to house each individual message that should be sent
    return response_messages

# Run Test
# print "first call"
# print coach_response('coach')
# print "second call"
# print coach_response(5)
# print "third call"
# print coach_response(3)

# tag_one = "h5"
# tag_one_text = 'Habit 3: Put First Things First'
# tag_two = "h6"
## ---------------------------------------------------------- ##
