# Dad Jokes

![Responsive screenshot](/docs/readme-images/responsive-screen.png)

# The purpose with this project

Dad Jokes is a console based application that accommodates individuals that are either interested in quick amusement of silly jokes or individuals that wants to share their silly jokes with other users. The user interface is text based and it is run from a text terminal or other types of command-in interfaces. 

The application has two options at start that either lets the user read and rate a joke or submit a joke together with their name.

Target audience: All individuals that wants to read and rate a silly joke and all individuals that wants to submit a joke for future rating.

This project is the third of five milestone projects that needs to be completed in order for me to receive a diploma in Software Development from The Code Institute https://codeinstitute.net/

Required technologies for this project: Python

A live version of this project can be found at this url: https://dad-jokes-1.herokuapp.com/

# Table of Content

+ [UX](#ux "UX")
  + [User Demographic](#user-demographic "User Demographic")
  + [User Stories](#user-stories "User Stories")
    + [User reading](#user-reading "User reading")
    + [User submitting](#user-submitting "User submitting")
  + [User Goals](#user-goals "User goals")
  + [Project Requirements](#project-requirements "Project Requirements")
  + [Design diagram](#design-diagram "Design diagram")
+ [Features](#features "Features")
  + [Existing Features](#existing-features "Existing Features")
    + [Start Read and Rate](#start-read-and-rate "Start read and rate")
    + [Start submit joke](#start-submit-joke "Start submit joke")
  + [Features Left to Implement](#features-left-to-implement "Features Left to Implement")
+ [Technologies used](#technologies-used "Technologies used")
  + [Data storage](#data-storage "Data Storage")
+ [Testing](#testing "Testing")
  + [Bugs during development](#bugs-during-development "Bugs during development")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [Development and Deployment](#development-and-deployment "Development and Deployment")
+ [Content](#content "Content")
+ [Media](#media "Media")
+ [Credits](#credits "Credits")

## UX

### User Demographic

This application is ment for:

 - All individuals that wants amusements gotten by reading short silly jokes.
 - All individuals that wants to share silly jokes and have the rated by other users.

### User Stories

I have divided the user stories for this application in to two different sections, User Reading and User Submitting. The scenarios do not differ much between Old users and New users.

#### User reading

 - I want to read a silly joke.
 - I want to rate a silly joke.
 - I want to see who submitted silly jokes.
 - I want to see the rating my submitted joke has. (Old user)
 - I want to see if there is any more jokes since last time I used the application (Old user)

#### User submitting

 - I want to submit a silly joke.
 - I want other users to read my silly joke.
 - I want other users to rate my silly joke.

### User Goals

To get amused by silly jokes for a short period of time OR submit silly jokes.

### Project Requirements

Python application using libraries/API and deployed to a cloud-based platform.

### Design diagram

Dad Jokes is a console based application. For that reason no work was put in to graphical design. Instead focus was put on creating a diagram of the entire application and use that as the base for the code. The diagram also include the Google Sheet used for data storage.


This is the initial diagram:

![Intial diagram](/docs/readme-images/p3-diagram-screen.png)

During the development process a few things were changed in the diagram. The main reason for this was that I had done a flaw in the design of the Google Sheet. I had placed the calculation formula for average score on jokes inside the sheet. I never got this to work properly so that column was eventually removed and the calculation is done in the application instead.

After the final alterations the final application diagram looks like this:

![Final diagram](/docs/readme-images/p3-diagram-final-screen.png)

[Back to top](#dad-jokes)

## Features 

Dad Jokes consists of two features. The user chooses the option of feature from the start section of the application. The features are:

 - Read and rate a joke
 - Submit a joke

### Existing Features

#### Start read and rate

The user starts the read and rate option from the start section of the application. To read and rate the number 1 needs to be entered followed by the enter key.

![Start read and rate](/docs/readme-images/start-read-screen.png)

After selection the user is presented with a random selected joke from the Google sheet. The user also sees the rating of the joke. The user is also asked to rate the joke by entering a number between 1 and 5.

![Read and rate screen](/docs/readme-images/read-rate-screen.png)

When the rating has been entered the user is taken to the last section of this option. Here the user can choose to read and rate a new joke, restart the application or quit the application.

![Read and rate screen](/docs/readme-images/end-read-rate-screen.png)

If j is selected the user will receive another joke and rate, if r is pressed the application starts over from the start selection screen and q will terminate the application.

#### Start submit joke

The user starts the submit option from the start section of the application. To submit a joke the number 2 needs to be entered followed by the enter key.

![Start submit](/docs/readme-images/start-read-screen.png)

After the selection the user is presented with an instruction to follow the steps and enter a name or a nickname.

![Enter name](/docs/readme-images/enter-name-screen.png)

When name is entered the user is presented with instructions on how to write to make it easier for other users and prompted to enter their joke.

![Enter name](/docs/readme-images/enter-joke-screen.png)

When the joke has been submitted the user is taken to the last section of this option. Here the user can choose to submit another joke, restart the application or quit the application.

![Enter name](/docs/readme-images/end-submit-screen.png)

If s is selected the user will restart the submit function, if r is pressed the application starts over from the start selection screen and q will terminate the application.

## Features Left to Implement

Future versions of this application will contain a graphical user interface and a capability for users to search and find the rating of their jokes.

[Back to top](#dad-jokes)

## Technologies and libraries used

Main languages

- [Python](https://en.wikipedia.org/wiki/Python_programming_language)
- [HTML](https://en.wikipedia.org/wiki/HTML) - Provided in the Code Institute template
- [CSS](https://en.wikipedia.org/wiki/CSS) - Provided in the Code Institute template
- [JavaScript](https://en.wikipedia.org/wiki/javascript) - Provided in the Code Institute template

Python libraries and api used

- [Sys](https://docs.python.org/3/library/sys.html)
- [Random](https://docs.python.org/3/library/random.html)
- [Google auth](https://google-auth.readthedocs.io/en/master/index.html)
- [Termcolor](https://pypi.org/project/termcolor/)

### Data storage

Jokes, submitted jokes, sumbmitter name and scores are fetched and stored in a Google Sheet using:

- [Google Drive API](https://developers.google.com/drive/api)
- [Google Sheet API](https://developers.google.com/sheets/api)



## Testing 

Testing has been conducted continuously during the development process. Manual testing has been conducted by the author and my mentor [Martina Terlevic](https://www.linkedin.com/in/martinaterlevic/). Read more about bugs during development and unfixed bugs for more information.



### Bugs during development

- Using Colorama library but my tests are not working. When I do a print syntax with the provided syntax to change the font color "Hello World" is not printing.
  - <i>Used the wrong syntax. Needed to add a "+" sign before the string</i>
- Pure strings are using the selected colors but all prints from the worksheet are still white and I get a syntax error.
  - <i>Tried Termcolor library instead of Colorama library and it did the trick</i>
- Get error messages when I try to access a specific row in the worksheet
  - <i>Used the wrong syntax for the library Gspread. Tryed to install and import a different library but that was also problematic. Eventually I found the syntax for the Gspread library and it worked.</i>
- Not able to add new rating with total rating
  - <i>The variables were strings, converted them to int's and it worked</i>
- Not able to get a proper error message when rating not entered correctly
  - <i>Used an if/else statement to check and return if input is faulty</i>
- The worksheet is not updating correctly. Can't figure out why.
  - <i>Went back to look at Love Sandwiches and created a function that updates the worksheet based on that project</i>
- Can't figure out how to correctly copy the formula needed in the spreadsheet to get avarage rating.
  - <i>Will try to do the calculation inside Python instead. Update: Did overhaul all that had to do with avarage score. Removed the calculation of score from the spreadsheet and did the calculation in run.py instead</i>

### Validator Testing 

The code has also been tested by using PEP8 Online http://pep8online.com/.

Final testing warned about long lines. This has been corrected and the code passes without any issues.

### Unfixed Bugs



 [Back to top](#dad-jokes)

## Development and Deployment

Deployment description

## Content 

- All text content in this game has been produced by the author.
- Credit to jokes content

## Media

Media description

## Credits 

### For code inspiration, design inputs, help and advice.

Text 

 - link
 - link
 - link

### Acknowledgment

 - Person 1
 - Person 2

 [Am I Responsive](http://ami.responsivedesign.is/) was used to create the image on top of this ReadMe

[Back to top](#dad-jokes)