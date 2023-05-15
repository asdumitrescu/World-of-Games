# **World of Games**

## Overview

World of Games is a collection of three command-line games: 

#### Memory Game, Guess Game, and Currency Roulette. 

This project also includes a Flask web service for keeping track of scores.

***
World of Games is a Python project that can be run on any platform that supports Python 3.9 or later. The project is structured as follows:
* #### World-Of-Games/
  * #### |-- Games/
    * |   |-- CurrencyRoulette.py
    * |   |-- GuessGame.py
    * |   |-- MemoryGame.py
  * #### |-- Scores/
    * |   |-- Dockerfile
    * |   |-- MainScores.py
    * |   |-- Score.py
    * |   |-- Scores.txt
    * |   |-- docker-compose.yml
  * #### |-- tests/
    * |   |-- e2e.py
* |-- Live.py
* |-- MainGame.py
* |-- Replay.py
* |-- Utils.py
* |-- Jenkinsfile
* |-- name.txt
***
### Games

This folder contains the modules of the three games:

#### 1. MemoryGame.py: A game that involves remembering the randomly-generated number shown on the screen.

                  The computer will give random numbers from 1 to 100 in the amount of difficulty the user chose and 
                  will show it on the terminal for 0.7 seconds then the terminal will clear.
                  Example: 23 42 50 98       
                  Last example was for difficulty level 4 selected.
                  And the user will have to remember the numbers and enter them down in the same order as shown on the screen.

#### 2. GuessGame.py: A game that involves guessing a number between 1 - Difficulty level selected.

                 The computer will generate a random number between 1 to the difficulty 
                 level selected by the user and you have to guess which number the computer generated.
3. CurrencyRoulette.py: A game that involves guessing the value of a random amount of Shekels that it can be from 1 - 100
                        into dollar currency.
                        
***
### Scores

This folder contains the implementation of a Flask web service for keeping track of scores. 
The implementation includes a Dockerfile that sets up a Python 3.9 environment and installs Flask,
as well as a docker-compose.yml file that builds and deploys the service. The Dockerfile copies the MainScores.py and Utils.py 
files into the container, along with the Scores.txt . The docker-compose.yml file defines
a container named 'flask_app' that mounts local files as volumes, exposes the container's port 5000 to host port 8777,
and connects to a custom network with a static IP address.
***
### tests

This folder contains an end-to-end (e2e) test script for testing the web service.

***
### **Main directory World Of Games files:**

#### **Live.py** 
This file contains the main menu and game loop for the three games.
***
#### **MainGame.py**

This file contains the logic for starting a game based on the user's selection.
***
#### **Replay.py**

This file contains the logic for asking the user if they want to play again after a game has ended.
***
#### **Utils.py**

This file contains utility functions used by the games and the web service.
***

#### Jenkinsfile

This file contains the pipeline for building, testing, 
and deploying the Scores service and running end-to-end tests 
using the e2e.py file and deleting the containers and all the other services and dependecies created in the pipeline,
finally pushing the image to docker hub.
***
#### **name.txt**

This file contains the user's name.
***
### Web Service

The web service is a Flask application that runs an html code and will show the scores inside a browser.

The main route (/): Accepts a GET request and returns 
an HTML page that displays the user's name and score from 
the "name.txt" and "scores.txt" files, respectively.

It can be started by running the MainScores.py file located in Scores folder as following:

Open terminal ===> Navigate to Scores folder ===> Run the following command: 

#### python3 MainScores.py

After running the above command you can access it here: http://localhost:5000/

It can be also runned inside a docker container by navigating to Scores folder and running the following command:

#### docker-compose build

#### docker-compose up

You can access it after running the above commands here: http://172.25.0.5:5000

***
## **How to Use**

To start the games, please run the following command in your terminal after you navigate to
the main directory of the project:

#### python3 MainGame.py  

This will start the main menu, where you have too enter your name and where you will
select the game you want to play with the desired difficulty.


***
To run the end-to-end test, please run the following command in your terminal after navigating to tests folder
and after you have the web service running locally: 

#### python3 e2e.py
***
### Project Requirments

To install the requirements for this project, please run the following command in your terminal:

**pip install -r requirements.txt**

This will install all the required dependencies, including Flask and Selenium. 
Make sure you are in the root directory of the project before running this command.
***
## We hope you enjoy playing World of Games!