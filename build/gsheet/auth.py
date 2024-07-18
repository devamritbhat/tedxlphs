import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = [
    "https://spreadsheets.google.com/feeds",
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

sheet_creds = ServiceAccountCredentials.from_json_keyfile_name("build/gsheet/sheet1.json", SCOPES)
sheet_client = gspread.authorize(sheet_creds)
sheet_spreadsheet = sheet_client.open("TEDxYOUTH@LPHS REGISTRATIONS")
response = sheet_spreadsheet.worksheet("Tickets 2024")

def queryResponse(tm, fn, ls, cno, email, age, quantity, seats, amt, tr, cnt):
    response.batch_update([{
    'range': 'A'+cnt+':K',
    'values': [[tm, fn, ls, cno, email, age, quantity, seats, amt, tr]]
}])
    