# Dad Jokes

![Responsive screenshot](/docs/readme-images/placeholder-1000-700.jpg)

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
    + [Joke Screen](#joke-screen "Joke Screen")
    + [Submit Score Screen](#submit-score-screen "Submit Score Screen")
    + [Joke Restart Screen](#joke-restart-screen "Joke Restart Screen")
    + [Submit Name Screen](#submit-name-screen "Submit Name Screen")
    + [Submit Joke Screen](#submit-joke-screen "Submit Joke Screen")
    + [Submit Restart Screen](#submit-restart-screen "Submit Restart Screen")
    + [End Screen](#end-screen "End Screen")
  + [Features Left to Implement](#features-left-to-implement "Features Left to Implement")
+ [Technologies used](#technologies-used "Technologies used")
+ [Testing](#testing "Testing")
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

Start read and rate

The user starts the read and rate option from the start section of the application. To read and rate the number 1 needs to be entered followed by the enter key.

![Start read and rate](/docs/readme-images/start-read-screen.png)

After selection the user is presented with a random selected joke from the Google sheet. The user also sees the rating of the joke. The user is also asked to rate the joke by entering a number between 1 and 5.

![Read and rate screen](/docs/readme-images/read-rate-screen.png)

When the rating has been entered the user is taken to the last section of this option. Here the user can choose to read and rate a new joke, restart the application or quit the application.

![Read and rate screen](/docs/readme-images/end-read-rate-screen.png)

#### Joke Screen

Description 

 - Options

![Game Screen](/docs/readme-images/placeholder-900-630.jpg)

#### Submit score screen

Description

 - Options

![About us Section part 1](/docs/readme-images/placeholder-900-630.jpg)

#### Joke restart screen

Description

 - Options

![About us Section part 1](/docs/readme-images/placeholder-900-630.jpg)

#### Submit name screen

Description

 - Options

![About us Section part 1](/docs/readme-images/placeholder-900-630.jpg)

#### Submit joke screen

Description

 - Options

![About us Section part 1](/docs/readme-images/placeholder-900-630.jpg)

#### Submit restart screen

Description

 - Options

![About us Section part 1](/docs/readme-images/placeholder-900-630.jpg)

#### End screen

Description

 - Options

![About us Section part 1](/docs/readme-images/placeholder-900-630.jpg)

### Features Left to Implement

- text

[Back to top](#quickmem)

## Technologies and libraries used

- color https://pypi.org/project/termcolor/
- Pygsheets https://pygsheets.readthedocs.io/en/stable/

- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/javascript)

## Testing 

- text option 1

  - Solution

- Text option 2

  - Solution


### Validator Testing 

Testing text and links

### Unfixed Bugs

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

 [Back to top](#quickmem)

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

[Back to top](#quickmem)