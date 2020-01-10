import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread.exceptions import CellNotFound
import json

# use creds to create a cl  xient to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# SHEET_NAME = 'Menora Mivtahim - Events - test'
SHEET_NAME = 'Menora Mivtahim - Events'

def _parse_event(event):
    return list(reversed(list(event.values())))

def write_to_sheet(event):
    sheet = client.open(SHEET_NAME).sheet1
    # Extract and print all of the values
    try:
        sheet.find(event['datetime'])
        print("The event already been recorded")
        return
    except CellNotFound:
        print("Adding new event")
        event = _parse_event(event)
        sheet.append_row(event, value_input_option='RAW')
