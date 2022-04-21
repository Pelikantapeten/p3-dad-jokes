# Imports
import gspread
from google.oauth2.service_account import Credentials
from termcolor import colored
import random

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
    print(colored(('Wellcome to Dad Jokes!\n'), 'cyan'))
    print(colored(('Endulge yourself in very silly random jokes'), 'cyan'))
    print(colored(('or contribute with a joke of your own making.\n'), 'cyan'))
    print(colored(('Enter 1 to read and rate a joke'), 'cyan'))
    print(colored(('Enter 2 to submit a joke\n'), 'cyan'))


def user_choice():
    """
    Function that determines if the user wants to read and rate
    a joke or want to submit a joke
    """
    choice = input('Please, make your choice (1 or 2)\n')
    if choice == '1':
        display_random_joke()
    elif choice == '2':
        print('Hello choice 2')
    else:
        print('You must choose 1 or 2')
        return user_choice()


def display_random_joke():
    """
    Function that displays a random joke from the spreadsheet
    if user selects option 1
    """
    list_of_lists = SHEET.worksheet('jokes').col_values(5)
    del list_of_lists[0]
    displayed_joke = random.choice(list_of_lists)
    print('\n', displayed_joke)
    cell = SHEET.worksheet('jokes').find(displayed_joke)
    joke_rating = SHEET.worksheet('jokes').cell(cell.row, (cell.col - 1)).value
    print('\nThis joke is rated ', joke_rating)


def main():
    """
    Main function that runs the applications functions
    """
    intro_dad_joke()
    user_choice()


main()

