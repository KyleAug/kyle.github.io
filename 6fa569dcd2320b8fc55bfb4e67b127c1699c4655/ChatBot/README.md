# ChatBot
*Created by Kyle Auger*

# Set Up
Paste the below commands into terminal to install the appropriate modules.
```
sudo pip install oauth2client
```
```
sudo pip install --upgrade google-api-python-client
```
```
sudo pip install beautifulsoup4
```

# Run
Run the following command in a Terminal shell.
```
bash X0_run_me.bash
```
This will start the 'X1_run_loop.py' file.


# File Structure

## X0: Administrative Py Files & Bash Files
* X0_run_me.bash
* X0_administrative.py

## X1: Start Loop
* X1_run_loop.py
Defines the loop that the ChatBot program runs and its updating frequency.

## X2 Main Menu
* X2_start_action_thread.py
The support that creates a thread to execute a specific request.
* X2_main_menu.py
The program's "main menu", handling and passing variables to whichever mode is requested.

## X3 Program Modes
The landing page for each mode of the program. The files have two functions for each mode:
1. Check the category (e.g. request_type) is X and returns a T/F
2. Formulates a response to the request
* X3_responses_coach.py
* X3_responses_wallet.py
* X3_responses_greetings_farewells.py

## X4 Content Wrappers
* X4_read_coach_content.py
Uses BeautifulSoup to read HTML.
* X4_update_coach_content.py
Pulls the latest version of the ChatBot document from Google Drive.

## Google APIs
* gmail_api.py
An API wrapper designed to reads & sends email messages.
* gdrive_api.py
An API wrapper designed to connect to Google Drive for the purpose of reading the ChatBot google doc.

## Text Files
* ChatBot.html
The local copy of the ChatBot document in HTML.





---
