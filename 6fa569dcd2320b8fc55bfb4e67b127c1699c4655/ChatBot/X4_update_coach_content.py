
## Modules to Import ---------------------------------------------------------- ##
# from update_coach_content import update_coach_content, coach_file

## Imported Modules ---------------------------------------------------------- ##
from X0_administrative import logger, status
from gdrive_api import gdrive_export_doc, deleteContent

## ---------------------------------------------------------- ##
# Updates the text file holding the Coach content
coach_file = {'file_id': '1Gpwxee8D6W1ryIcpTlr4E0iEUwxNo9hykyLXzBE27Nc',
    'mimeType': 'text/html',
    'export_filename': 'ChatBot.html'
    }

def update_coach_content(export_filename, file_id, mimeType):
    # Deletes the existing text in the output file
    deleteContent(export_filename)
    # Retrieves the latest text from the server and writes to the output file
    gdrive_export_doc(file_id, export_filename, mimeType)
    logger.info("Updated Coach content from the server.")
    return
# Run
# update_coach_content(coach_file['export_filename'], coach_file['file_id'], coach_file['mimeType'])
