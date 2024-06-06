# This code reads a value from a Google Sheet and compares it with a hardcoded Net Premium value.
# The value from the Google Sheet is expected to be a number in cell A1.
# The hardcoded Net Premium value is compared with the value from the Google Sheet.
# The comparison result is printed out indicating whether the Net Premium value is greater than,
# less than, or equal to the value in the Google Sheet.

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

# Path to the credentials JSON file
credentials_file = 'B:\\CLAP GROW\Clap_Grow_Assignment\\credentials.json'
# Check if the credentials file exists
if not os.path.exists(credentials_file):
    raise FileNotFoundError(f"The credentials file was not found at {credentials_file}")

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Authorize the client using the credentials file
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
client = gspread.authorize(credentials)

# Open the Google Sheet
spreadsheet = client.open("Insurance Premium Comparison")  # Replace with your Google Sheet name
sheet = spreadsheet.sheet1  # Use the first sheet

# Read the number from the Google Sheet
google_sheet_value_str = sheet.cell(1, 1).value  # Assumes the number is in cell A1
google_sheet_value = int(google_sheet_value_str.replace(",", ""))

# Net Premium from the document
net_premium = 2895421

# Compare the values
if net_premium > google_sheet_value:
    print(f"Net premium ({net_premium}) is greater than the value in the Google Sheet ({google_sheet_value}).")
elif net_premium < google_sheet_value:
    print(f"Net premium ({net_premium}) is less than the value in the Google Sheet ({google_sheet_value}).")
else:
    print(f"Net premium ({net_premium}) is equal to the value in the Google Sheet ({google_sheet_value}).")
