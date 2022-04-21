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


def intro_dad_joke():
    """
    Application introduction that explains the purpose
    of the application and gives instructions to the user.
    """
    print(colored(('Wellcome to Dad Jokes!'), 'cyan'))
    print(colored(('Placeholder text with instructions'), 'cyan'))
    print(colored(('Placeholder text with instructions'), 'cyan'))
    print(colored(('Enter 1 to read and rate a joke'), 'cyan'))
    print(colored(('Enter 2 to submit a joke'), 'cyan'))


def user_choice():
    """
    Function that determines if the user wants to read and rate
    a joke or want to submit a joke
    """
    print('Hello World!')


def main():
    """
    Main function that runs the applications functions
    """
    intro_dad_joke()
    user_choice()


main()
