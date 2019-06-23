# Importing required libraries
from apiclient import discovery, errors
from httplib2 import Http
from oauth2client import file, client, tools
import base64
import re
import time
import dateutil.parser as parser
from datetime import datetime
import smtplib

### Basic Logging Details
import logging
logging.basicConfig(
    filename='/Users/kyleauger/ChatBot/ChatBot_Log.log',
    level=logging.INFO,
    format = '%(asctime)s -- %(levelname)s -- %(message)s')

# Recieves and reads incoming emails
## currently limited to snippets (reading of the entire message body is not working)
### If no messages: returns FALSE. Else, returns the message.
def gmail_read():
	# Creating a storage.JSON file with authentication details
	SCOPES = 'https://www.googleapis.com/auth/gmail.modify' # we are using modify and not readonly, as we will be marking the messages Read
	store = file.Storage('/Users/kyleauger/ChatBot/gmail_api_storage.json')
	creds = store.get()
	if not creds or creds.invalid:
	    flow = client.flow_from_clientsecrets('/Users/kyleauger/ChatBot/gmail_api_secret.json', SCOPES)
	    creds = tools.run_flow(flow, store)
	GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

	user_id = 'me'
	label_id_one = 'INBOX'
	label_id_two = 'UNREAD'

	# Getting all the unread messages from Inbox
	# labelIds can be changed accordingly
	unread_msgs = GMAIL.users().messages().list(userId='me',labelIds=[label_id_one, label_id_two]).execute()

	# We get a dictonary. Now reading values for the key 'messages'
	try:
		mssg_list = unread_msgs['messages']
	except KeyError:
		return False, False

	final_list = [ ]

	for mssg in mssg_list:
		m_id = mssg['id'] # get id of individual message
		message = GMAIL.users().messages().get(userId=user_id, id=m_id).execute() # fetch the message using API
		payld = message['payload'] # get payload of the message
		headr = payld['headers'] # get header of the payload

		for one in headr: # getting the Sender
			if one['name'] == 'From':
				msg_from = one['value']
				# checking the sender
				if (msg_from == '4848440318@vzwpix.com' or '4848440318@vtext.com'):
					# fetching the sender
					reply_user = str(msg_from)
					# fetching message snippet
					final_list.append(message['snippet'])
				else:
					pass
		# getting the date
		for two in headr:
			if two['name'] == 'Date':
				msg_date = two['value']
				logging.debug(msg_date)
				# date_parse = (parser.parse(msg_date))
				# m_date = (date_parse.date())
				# temp_dict['Date'] = str(m_date)
			else:
				pass

		# This will mark the messages as read
		GMAIL.users().messages().modify(userId=user_id, id=m_id,body={ 'removeLabelIds': ['UNREAD']}).execute()
	# print ("Total unread messages in inbox: ", str(len(mssg_list)))
	# print ("Total messaged retrived: ", str(len(final_list)))
	return reply_user, final_list

# Sends an outgoing email

from email.mime.text import MIMEText

# Sends an outgoing email
def gmail_send(recipient, content):
    gmail_user = "ETHnotification@gmail.com"
    gmail_pwd = "Ethereum"
    FROM = "ETHnotification@gmail.com"
    TO = recipient if type(recipient) is list else [recipient]
    message = MIMEText(content.encode('utf-8'), _charset='utf-8')
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message.as_string())
        server.close()
        return True
    except:
        return False
# Run
# print gmail_send("4848440318@vzwpix.com", u'\u0235')
