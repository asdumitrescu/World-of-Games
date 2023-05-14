# This section imports the necessary modules and defines some constants
import os
import time

# some variables that i store my paths for the files in order to be used in the program in different modules
SCORES_FILE_NAME = "./Scores/Scores.txt"
SCORES_FILE_FLASK = "./Scores.txt"
BAD_RETURN_CODE = "ERROR CODE 214"


# This function waits for 0.7 seconds and clears the screen based on the OS being used
def Screen_cleaner():
    time.sleep(0.7)
    if os.name == 'nt':          # Check if the OS is Windows
        os.system('cls')         # Clear the screen using "cls" command
    else:                        # if the if block its not returning True then it will use it for linux
        os.system('clear')       # Clear the screen using "clear" command

# This function reads the contents of a source file, writes them to a destination file, and then clears the source file
