import os  # import the "os" module
from Utils import SCORES_FILE_NAME  # import the "SCORES_FILE_NAME" constant from the "Utils" module

# define a function named "add_score" that takes one argument: lvl_sel
def add_score(lvl_sel):
    POINTS_OF_WINNING = (lvl_sel * 3) + 5  # calculate the points of winning based on the difficulty level

    if os.path.exists(SCORES_FILE_NAME):  # check if the score file exists
        with open(SCORES_FILE_NAME, 'r') as scores:  # open the score file for reading
            current_score = scores.read().strip()  # read the current score and remove any whitespace
        if current_score == '':  # check if the score file is empty
            current_score = 0  # set the current score to 0
        else:
            current_score = int(current_score)  # convert the current score to an integer
    else:
        current_score = 0  # if the score file does not exist, set the current score to 0

    update_score = current_score + POINTS_OF_WINNING  # calculate the updated score
    with open(SCORES_FILE_NAME, 'w') as scores:  # open the score file for writing
        scores.write(str(update_score))  # write the updated score to the score file as a string
    return update_score  # return the updated score
