# Imports
import gspread
from google.oauth2.service_account import Credentials
from termcolor import colored

# This was inspired by and borrowed from 
# Code Instituet Love Sandwiches project
# https://github.com/Code-Institute-Solutions/love-sandwiches-p4-sourcecode
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('dad_jokes')

jokesTest = SHEET.worksheet('jokes')

allData = jokesTest.get_all_values()

print(colored((allData), 'green'))