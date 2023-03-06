import os
from flask import Flask
from Utils import BAD_RETURN_CODE, LAST_SCORES, SCORES_FILE_NAME


app = Flask(__name__)


@app.route('/')
def score_server():
    with open('../name.txt', 'r+') as file:
        user_name = file.read()
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r') as scores_file:
            score = scores_file.readline().strip()
        return "<html><head><title>Scores Game</title><meta http-equiv='refresh' content='10'></head><body><h1>Hello " \
            + user_name + " your score is:<div id='score'>" + score + "</div></h1></body></html>"

    else:
        return "<html><head><title>Scores Game</title></head><body><h1><div id='score' style='color:red'>" \
            + str(BAD_RETURN_CODE) + "</div></h1>"


@app.route('/last_score')
def old_score():
    with open('../name.txt', 'r+') as file:
        user_name = file.read()
    if os.path.exists(LAST_SCORES):
        with open(LAST_SCORES, 'r') as scores_file:
            LAST_SCORE = scores_file.readline().strip()
        return "<html><head><title>Scores Game</title><meta http-equiv='refresh' content='30'></head><body>" \
               "<h1>Hello " + user_name + " your last score was:<div id='score'>" + LAST_SCORE + "</div></h1></body></html>"

    else:
        return "<html><head><title>Last Scores Game</title></head><body><h1><div id='score' style='color:red'>" \
            + str(BAD_RETURN_CODE) + "</div></h1>"


app.run(host='127.0.0.1', debug=True, port=5000)
