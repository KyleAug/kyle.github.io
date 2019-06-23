from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import io
from apiclient.http import MediaIoBaseDownload

# If modifying these scopes, delete the file token.json.
# SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
# SCOPES = 'https://mail.google.com/'

def gdrive_export_doc(file_id, export_filename, mimeType):
    # Authorizes Credentials
    store = file.Storage('gdrive_api_token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('gdrive_api_credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    drive_service = build('drive', 'v3', http=creds.authorize(Http()))

    # Calls Google Drive Version 3 API
    request = drive_service.files().export(fileId=file_id, mimeType=mimeType)
    fh = io.FileIO(export_filename, 'wb') # Exports the content to a specific file
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        # print status # print "Download "+str(int(status.progress() * 100))
        # print "Download %d%%." % int(status.progress() * 100)
    return


def deleteContent(fName):
    with open(fName, "w"):
        pass
