# Dad Jokes

![Responsive screenshot](/docs/readme-images/placeholder-1000-700.jpg)

# The purpose with this project

Text to describe the purpose

A live version of the project can be found here: https://dad-jokes-1.herokuapp.com/

# Table of Content

+ [UX](#ux "UX")
  + [User Demographic](#user-demographic "User Demographic")
  + [User Stories](#user-stories "User Stories")
    + [New Users](#new-users "New Users")
    + [Old Users](#old-users "Old Users")
  + [User Goals](#user-goals "User")
  + [Project Requirements](#project-requirements "Project Requirements")
  + [Design diagram](#design-diagram "Design diagram")
+ [Features](#features "Features")
  + [Existing Features](#existing-features "Existing Features")
    + [Start Screen](#start-screen "Start Screen")
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

This game is ment for:

 - All individuals, regarding age, that wants to play a challenging game.

### User Stories

The user stories

#### New users

 - Text

#### Old users

 - Text

### User Goals

 - Text

### Project Requirements

 - Requirements from CI

### Design diagram

Text and flowchart



Screen

![Screen](/docs/readme-images/placeholder-900-630.jpg)


[Back to top](#quickmem)

## Features 

Text that describes the features

 - screen 1
 - screen 2
 - etc

Descriptive text

### Existing Features

#### Start

Description

 - Option 1
 - Option 2

![Start](/docs/readme-images/placeholder-900-630.jpg)

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