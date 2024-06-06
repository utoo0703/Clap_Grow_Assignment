
#  Clap Grow Assignment- Insurance Premium Comparison

This repository contains three Python scripts for comparing insurance premium values:

1. **compare_premium_hardcoded.py**: This script compares a hardcoded net premium value with a value retrieved from a Google Sheet. It demonstrates basic comparison logic.

2. **compare_premium_from_PDF.py**: This script reads a net premium value from a PDF document and compares it with a value retrieved from a Google Sheet. It utilizes regular expressions to extract the value from the PDF.

3. **list_gsheet_files.py**: This script lists all available spreadsheets accessible by the authorized client in the Google Sheets API. It helps in verifying the availability of spreadsheets.

## Usage

### compare_premium_hardcoded.py

This script compares a hardcoded net premium value with a value retrieved from a Google Sheet. Run the script to see the comparison result in the console.

### compare_premium_from_PDF.py

This script reads a net premium value from a PDF document and compares it with a value retrieved from a Google Sheet. Run the script to see the comparison result in the console.

### list_gsheet_files.py

This script lists all available spreadsheets accessible by the authorized client in the Google Sheets API. Run the script to see the list of available spreadsheets in the console.

## Google Sheets API Authentication

The Google Sheets API requires authentication to access Google Sheets data. This authentication is handled using service account credentials, which are stored in a JSON file provided by Google.

To authenticate with the Google Sheets API in these scripts, you need to obtain a service account credentials JSON file from the Google Cloud Console and place it in the project directory with the name `credentials.json`.

The `credentials.json` file contains information about the service account, including the private key, client email, and other authentication details. This file is securely used by the scripts to authorize access to Google Sheets data.


## Screenshots
![image](https://github.com/utoo0703/Clap_Grow_Assignment/assets/78578594/194e4e7f-0156-49dc-91a2-e0239b512c9c)




