import os  # import the "os" module
from flask import Flask  # import the "Flask" class from the "flask" module
from Utils import BAD_RETURN_CODE, LAST_SCORES_FLASK, SCORES_FILE_FLASK  # import some constants from the "Utils" module

app = Flask(__name__)  # create a new Flask app instance

# define a route for the root URL "/"
@app.route('/')
def score_server():
    with open('./name.txt', 'r+') as file:  # open the "name.txt" file for reading and writing
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

host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
port = int(os.environ.get('FLASK_RUN_PORT', 5000))
debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

if __name__ == '__main__':
    app.run(host=host, debug=debug, port=port)