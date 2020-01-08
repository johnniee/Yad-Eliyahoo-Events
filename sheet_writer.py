import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a cl  xient to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)


def write_to_sheet(event):
    sheet = client.open("Menora Mivtahim - Events").sheet1
    # Extract and print all of the values
    try:
        cell = sheet.find(event['datetime'])
        print("The event already been recorded")
    except:
        print("Adding new event")
        sheet.append_row(event.values(), value_input_option='RAW')
