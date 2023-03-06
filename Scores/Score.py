import os

from Utils import SCORES_FILE_NAME


def add_score(lvl_sel):
    POINTS_OF_WINNING = (lvl_sel * 3) + 5

    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r') as scores:
            current_score = scores.read().strip()
        if current_score == '':
            current_score = 0
        else:
            current_score = int(current_score)
    else:
        current_score = 0

    update_score = current_score + POINTS_OF_WINNING
    with open(SCORES_FILE_NAME, 'w') as scores:
        scores.write(str(update_score))
    return update_score
