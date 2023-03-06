
import os
import time


SCORES_FILE_NAME = "Scores.txt"

BAD_RETURN_CODE = "ERROR CODE 214"
LAST_SCORES = "Last_scores.txt"



def Screen_cleaner():

    time.sleep(0.7)
    # Clear the screen
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for Linux and other Unix-like systems
        os.system('clear')


def transfer_and_clear_file(src_file, cp_file):
    with open(src_file, 'r') as scores:
        current_score = scores.read().strip()

    with open(cp_file, 'w') as scores:
        scores.write(current_score)

    with open(src_file, 'w') as scores:
        scores.write('')



