# Imports
import sys
import random
import gspread
from google.oauth2.service_account import Credentials
from termcolor import colored

# The scope was inspired by and borrowed from 
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
    if user selects option 1 and shows rating of that joke.
    """
    list_of_lists = SHEET.worksheet('jokes').col_values(5)
    del list_of_lists[0]
    displayed_joke = random.choice(list_of_lists)
    print('\n', displayed_joke)
    cell = SHEET.worksheet('jokes').find(displayed_joke)
    joke_rating = SHEET.worksheet('jokes').cell(cell.row, (cell.col - 1)).value
    print('\nThis joke is rated ', joke_rating)
    submitted_by = SHEET.worksheet('jokes').cell(cell.row, (cell.col - 4)).value
    print('And was submitted by: ', submitted_by)
    print(colored(('\nPlease rate this joke between 1 to 5\n'), 'cyan'))
    print(colored(('1 = not funny at all, 5 = Hillarious\n'), 'cyan'))
    
    def enter_rating():
        """
        Fuction that let's the user input rating for last joke and stores
        the rating in the worksheet.
        """
        user_rating = input('Your rating: ')
        if '1' <= user_rating <= '5':
            user_rating = int(user_rating)
            total_rating = SHEET.worksheet('jokes').cell(cell.row, (cell.col - 3)).value
            total_rating = int(total_rating)
            new_rating = (user_rating + total_rating)
            SHEET.worksheet('jokes').update_cell(cell.row, (cell.col - 3), new_rating)
            total_number_of_ratings = SHEET.worksheet('jokes').cell(cell.row, (cell.col - 2)).value
            total_number_of_ratings = int(total_number_of_ratings)
            new_total_ratings = (total_number_of_ratings + 1)
            SHEET.worksheet('jokes').update_cell(cell.row, (cell.col - 2), new_total_ratings)
            joke_end()
        else:
            print('You must enter a number between 1 and 5')
            enter_rating()
    enter_rating()


def joke_end():
    """
    End and restart function for read and rate a joke option
    """
    print(colored(('Thank you for reading and rating a joke!\n'), 'cyan'))
    print(colored(('What would you like to do now?\n'), 'cyan'))
    print(colored(('Enter "j" to read and rate another joke.'), 'cyan'))
    print(colored(('Enter "r" to restart the application'), 'cyan'))
    print(colored(('Enter "q" to quit\n'), 'cyan'))
    end_choice = input('Please, make your choice (j, r or q)\n')
    if end_choice == 'j':
        display_random_joke()
    elif end_choice == 'r':
        main()
    elif end_choice == 'q':
        sys.exit('The application has been closed')
    else:
        print('You must choose j, r or q')
        return end_choice()


def main():
    """
    Main function that runs the applications functions
    """
    intro_dad_joke()
    user_choice()


main()

