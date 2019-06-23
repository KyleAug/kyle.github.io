# The file has two functions for the Greeting & Farewell Requests mode:
    # Checks if the request is greeting or farewell
        # Returns True or False
    # Creates a Response
        # Returns a response_text
## ---------------------------------------------------------- ##
import random

greeting_keywords = ['hello', 'hi', 'hey', 'greetings', 'sup', "what's up"]
greeting_responses = ["sup", "hey", "*nods*", "hello"]
farewell_keywords = ['end', 'session', 'bye', 'cya', 'see you', 'later', 'exit', 'close']
# farewell_responses = ["Goodbye", "Talk to you later", "bye"]

## ---------------------------------------------------------- ##

def lower_case(content):
    return str(content).lower()

# Functions which need to be imported
def check_if_greeting_request(request_content):
    request_content = lower_case(request_content)
    for keyword in greeting_keywords:
        if keyword in request_content:
            return True
    else:
        return False

def check_if_end_session_request(request_content):
    request_content = lower_case(request_content)
    for keyword in farewell_keywords:
        if keyword in request_content:
            return True
    else:
        return False

# Need to add a function to exit the current mode
## ---------------------------------------------------------- ##


def greeting_response():
    return [random.choice(greeting_responses)]
