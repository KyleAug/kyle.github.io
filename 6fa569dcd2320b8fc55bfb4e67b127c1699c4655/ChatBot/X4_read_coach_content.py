# Uses BeautifulSoup to read HTML.
## Main Functions:
    # understand_the_request(request_content)
    # response_content_generator(tag_one, tag_one_id, tag_two)

## Modules to Import ---------------------------------------------------------- ##
# from X4_read_coach_content import understand_the_request, response_content_generator

## Imported Modules ---------------------------------------------------------- ##
from X0_administrative import logger, status
from bs4 import BeautifulSoup, NavigableString

## Allows the Terminal to Read UTF-8 ---------------------------------------------------------- ##
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

## Reads the Coach file with BeautifulSoup ---------------------------------------------------------- ##
with open('ChatBot.html','r') as file:
    html_doc = file.read()
# Run
# print html_doc
soup = BeautifulSoup(html_doc, from_encoding='UTF-8', features="html5lib")
# Run
# text = soup.get_text()
# print text

## Functions for understand_the_request() ---------------------------------------------------------- ##
def process_request_content(tag_one, request_content, tag_two):
    # Process integers
    try:
        request_content = int(request_content)
        tag_one_id = status.last_call_dict[request_content]
        logger.debug("Request Content: Option Number: "+str(request_content))
    # Process text
    except:
        try:
            # Searches for the header
            test_request = soup.find_all(tag_one, text=request_content)
            # If it cannot find the header
            if test_request == []:
                logger.warn("Requested content could not be found.")
                return False, None
            # If it found the header
            tag_one_id = test_request[0]['id']
            logger.debug("Request Content: Content Text: "+str(request_content))
        # Also if the requested tag isn't valid
        except:
            logger.warn("Requested content could not be understood.")
            return False, None
    # Succesful Return (pass_fail = True, tag_one_id = soup_id_number)
    return True, tag_one_id

## Functions for response_content_generator() ---------------------------------------------------------- ##
def get_list_of_tag_names(header_number):
    string = ''
    n = 1
    for header in soup.find_all(header_number):
        string += header.get_text() + '\n'
        # Saves the output data to the administrative dict
        logger.debug(str(n)+header.get_text())
        status.last_call_dict[n] = header['id']
        n += 1
    return string[:-1]
def between(cur, end):
    while cur and cur != end:
        if isinstance(cur, NavigableString):
            text = cur.strip()
            if len(text):
                yield text
        cur = cur.next_element
def get_text_between_tags(first_soup_object, second_soup_object):
    return ' '.join(text for text in between(first_soup_object.next_sibling, second_soup_object))
# Returns the two soup objects where text is needed in between
def get_next_object_under_tag(tag_one, tag_one_id, tag_two):
    # Ensures that any lesser tags aren't missed
    tag_three = "h" + str(int(tag_two[1])+1)
    tag_four = "h" + str(int(tag_three[1])+1)
    a = soup.find_all([tag_one, tag_two, tag_three, tag_four])
    returned_data = ''
    found_header = False
    for header in a:
        # Finds the tag directly after the targeted tag
        if found_header == True:
            next_object = header
            break
        # Finds the targeted tag
        if header['id'] == tag_one_id:
            first_tag_object = header
            found_header = True
    return first_tag_object, next_object
# Returns the text directly under a specific tag
def get_text_under_tag(tag_one, tag_one_id, tag_two):
    # Find the requested soup object & the very next tag
    first_soup_object, second_soup_object = get_next_object_under_tag(tag_one, tag_one_id, tag_two)
    return get_text_between_tags(first_soup_object, second_soup_object)
# Returns a list of the child headers under just that tag
def get_list_under_tag(tag_one, tag_one_id, tag_two):
    # Clears the administrative dict
    status.last_call_dict = {}
    a = soup.find_all([tag_one, tag_two])
    returned_data = ''
    found_header = False
    n = 1
    for header in a:
        if header['id'] == tag_one_id:
            found_header = True
            continue
        if found_header == True:
            if header.name == tag_one:
                break
            else:
                returned_data += header.get_text() + "\n"
                # Saves the output data to the administrative dict
                logger.debug(str(n)+header.get_text())
                status.last_call_dict[n] = header['id']
                n += 1
    return returned_data[:-1]

## ---------------------------------------------------------- ##
## Main Function - 1
def understand_the_request(request_content):
    ## Defines tag_one
    tag_one = "h" + str(status.tag)
    # Initial Coach request
    if tag_one == "h0":
        return True, "h0", "initialize", "h1"
    ## Define tag_two (the next tag)
    tag_two = "h" + str(int(tag_one[1])+1)
    ## Defines tag_one_id
    # In the process, confirms that the requested tag is a valid request (request_content == an int or text)
    pass_fail, tag_one_id = process_request_content(tag_one, request_content, tag_two)
    # Returns the approriate range of tags
    return pass_fail, tag_one, tag_one_id, tag_two
## ---------------------------------------------------------- ##
## Main Function - 2
def response_content_generator(tag_one, tag_one_id, tag_two):
    # If Coach is being initialized
    if tag_one_id == "initialize":
        return ["Main Menu:\n"+ get_list_of_tag_names("h1")]
    # Else, finds the specifically requested content
    response_content = []
    # Returns all text right underneath just that tag
    text_content = get_text_under_tag(tag_one, tag_one_id, tag_two)
    # Only adds to it if its not blank
    if text_content != '':
        response_content.append(text_content)
    # Returns a list of the child headers under just that tag
    list_content = get_list_under_tag(tag_one, tag_one_id, tag_two)
    # Only adds to it if its not blank
    if list_content != '':
        response_content.append(list_content)
    logger.debug(str(response_content))
    return response_content
# Run
# print response_content_generator(tag_one, tag_one_text, tag_two)
## ---------------------------------------------------------- ##


## Testing ---------------------------------------------------------- ##



# def convert_h_num(number):
#     return "h"+str(number)


# request_details = {'header_number': 5,
#                     'search_text': 'Habit 3: Put First Things First'}



# print first_soup_object.find_all("h6")
# Get the text/list of the headers underneath it.
# request_details['header_number'] += 1
# print get_list_of_tag_names(convert_h_num(request_details['header_number']))



# first_h1 = soup.h1
# print first_h1.find_next_sibling()
# header_list = ["h1", "h2", "h3", "h4", "h5", "h6"]
# def all_headers(header_list):
#     for header in soup.find_all(header_list):
#         print header.get('id'), header.name, header.get_text()
#         if header.name == "h6":
#             a = header.find_next_sibling
#             print a.get_text()
# all_headers(header_list)

## Find a specific item ---------------------------------------------------------- ##

# print soup.find(id='h.inmol6uv4sn')

# def find_soup_object(header, text):
#     return soup.find(header, text=text)
# print find_soup_object('h1', 'Document Guide')

# print soup.h1.get_text()
# first_header = soup.h1
# print first_header.name

# third_h1 = soup("h1", string="Financial")
# print third_h1
