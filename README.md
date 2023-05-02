# **World of Games**

## Overview

World of Games is a collection of three command-line games: 

#### Memory Game, Guess Game, and Currency Roulette. 

This project also includes a Flask web service for keeping track of scores.

Project Structure
The project is structured as follows:
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
    * |   |-- Last_scores.txt
    * |   |-- docker-compose.yml
  * #### |-- tests/
    * |   |-- e2e.py
* |-- Live.py
* |-- MainGame.py
* |-- Replay.py
* |-- Utils.py
* |-- Jenkinsfile
* |-- name.txt

### Games

This folder contains the implementation of the three games:

CurrencyRoulette.py: A game that involves guessing the value of a random amount of money in a foreign currency.
GuessGame.py: A game that involves guessing a randomly-generated number.
MemoryGame.py: A game that involves matching pairs of randomly-generated cards.

### Scores

This folder contains the implementation of a Flask web service for keeping track of scores. 
The implementation includes a Dockerfile that sets up a Python 3.9 environment and installs Flask,
as well as a docker-compose.yml file that builds and deploys the service. The Dockerfile copies the MainScores.py and Utils.py 
files into the container, along with the Scores.txt and Last_scores.txt files. The docker-compose.yml file defines
a container named 'flask_app' that mounts local files as volumes, exposes the container's port 5000 to host port 8777,
and connects to a custom network with a static IP address.

### tests

This folder contains an end-to-end (e2e) test script for testing the web service.

Live.py
This file contains the main menu and game loop for the three games.

MainGame.py
This file contains the logic for starting a game based on the user's selection.

Replay.py
This file contains the logic for asking the user if they want to play again after a game has ended.

Utils.py
This file contains utility functions used by the games and the web service.

Jenkinsfile
This file contains the pipeline for building, testing, and deploying the Scores service and running end-to-end tests using the e2e.py file.

name.txt
This file contains the user's name.

### Web Service

The web service is a Flask application that exposes a RESTful API for retrieving scores. The API has two endpoints:

/: Accepts a GET request and returns an HTML page that displays the user's name and score from the "name.txt" and "scores.txt" files, respectively.

/last_score: Accepts a GET request and returns an HTML page that displays the user's name and last score from the "last_score.txt" file.

This end-to-end test is triggered in Jenkins and uses Selenium to open a browser, navigate to the web service, and check that the displayed score
is between 1 and 1000. If the score is valid, the test passes; otherwise, it fails.

### Project Requirments

To install the requirements for this project, please run the following command in your terminal:

**pip install -r requirements.txt**

This will install all the required dependencies, including Flask and Selenium. 
Make sure you are in the root directory of the project before running this command.

