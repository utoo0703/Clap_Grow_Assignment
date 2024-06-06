# This code checks the existence of a credentials JSON file, authorizes a client using Google Sheets API,
# and lists all available spreadsheets accessible by the authorized client.
# The list of spreadsheets is printed out to check the available sheets for further operations.

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

# Path to the credentials JSON file
credentials_file = 'B:\\CLAP GROW\\credentials.json'

# Check if the credentials file exists
if not os.path.exists(credentials_file):
    raise FileNotFoundError(f"The credentials file was not found at {credentials_file}")

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

try:
    # Authorize the client using the credentials file
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    client = gspread.authorize(credentials)
except ValueError as e:
    print("An error occurred while authorizing the credentials:")
    print(e)
    exit(1)

# List all available spreadsheets
try:
    spreadsheets = client.openall()
    print("Available spreadsheets:")
    for spreadsheet in spreadsheets:
        print(spreadsheet.title)
except gspread.exceptions.APIError as e:
    print("An error occurred while listing the Google Sheets:")
    print(e)
    exit(1)
