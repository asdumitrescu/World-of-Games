import os  # import the "os" module
from flask import Flask  # import the "Flask" class from the "flask" module
from Utils import BAD_RETURN_CODE, LAST_SCORES_FLASK, SCORES_FILE_FLASK  # import some constants from the "Utils" module

app = Flask(__name__)  # create a new Flask app instance

# define a route for the root URL "/"
@app.route('/')
def score_server():
    with open('../name.txt', 'r+') as file:  # open the "name.txt" file for reading and writing
        user_name = file.read()  # read the user name from the file
    if os.path.exists(SCORES_FILE_FLASK):  # check if the score file exists
        with open(SCORES_FILE_FLASK, 'r') as scores_file:  # open the score file for reading
            score = scores_file.readline().strip()  # read the score from the score file and remove any whitespace
        # return an HTML response with the user name and score
        return "<html><head><title>Scores Game</title><meta http-equiv='refresh' content='10'></head><body><h1>Hello " \
            + user_name + " your score is:<div id='score'>" + score + "</div></h1></body></html>"
    else:
        # return an HTML response with an error message
        return "<html><head><title>Scores Game</title></head><body><h1><div id='score' style='color:red'>" \
            + str(BAD_RETURN_CODE) + "</div></h1>"

# define a route for the "/last_score" URL
@app.route('/last_score')
def old_score():
    with open('../name.txt', 'r+') as file:  # open the "name.txt" file for reading and writing
        user_name = file.read()  # read the user name from the file
    if os.path.exists(LAST_SCORES_FLASK):  # check if the last scores file exists
        with open(LAST_SCORES_FLASK, 'r') as scores_file:  # open the last scores file for reading
            LAST_S = scores_file.readline().strip()  # read the last score from the file and remove any whitespace
        # return an HTML response with the user name and last score
        return "<html><head><title>Scores Game</title><meta http-equiv='refresh' content='30'></head><body>" \
               "<h1>Hello " + user_name + " your last score was:<div id='score'>" + LAST_S + "</div></h1></body></html>"
    else:
        # return an HTML response with an error message
        return "<html><head><title>Last Scores Game</title></head><body><h1><div id='score' style='color:red'>" \
            + str(BAD_RETURN_CODE) + "</div></h1>"

# start the Flask app and listen for incoming requests
app.run(host='127.0.0.1', debug=True, port=5000)