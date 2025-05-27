import gspread
from google.oauth2.service_account import Credentials

def connect_to_google_sheet(creds_json_path, sheet_name):
    """
    Connects to a Google Sheet using a service account credentials JSON file.
    Args:
        creds_json_path (str): Path to the service account JSON credentials file.
        sheet_name (str): Name of the Google Sheet to connect to.
    Returns:
        gspread.Spreadsheet: The connected Google Sheet object.
    """
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    credentials = Credentials.from_service_account_file(creds_json_path, scopes=scopes)
    gc = gspread.authorize(credentials)
    sheet = gc.open(sheet_name)
    return sheet
