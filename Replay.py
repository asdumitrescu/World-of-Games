# First we import some modules from the python library that will be used in this module
import importlib
import Live
from Utils import Screen_cleaner, transfer_and_clear_file


#
# We define a function named "repeat_menu" that takes four arguments: user_name, lvl_sel, prev_game, and prev_difficulty
def repeat_menu(user_name, lvl_sel, prev_game=None, prev_difficulty=None):
    while True:  # start a loop that runs indefinitely
        # We made a variable named repeat for the repeat menu
        repeat = input("""Do you want to PLAY AGAIN the SAME GAME with the SAME DIFFICULTY, 
                         OR you want to PLAY ANOTHER GAME?

                                        To CONTINUE PLAYING the SAME GAME     
                                  with the SAME DIFFICULTY please type in >>>:   y.
                                                                                      =========      
                                        To Choose ANOTHER GAME please type in:   n.  
                                                                                  =============
                                        If you want to EXIT please type in:      q. 
                                                                               ================                  
                        >>> YOUR ANSWER HERE >>>:  """)

        if repeat == "" or repeat not in ['y', 'n', 'q']: # check if the user input is empty or not one of the expected values in the list
            print('Invalid input, try again!')  # Will display an error message in case the input is not in the list
            Screen_cleaner() # this is the function that we imported from Utils module that will clear the screen with 0.7 seconds sleep
            repeat_menu(user_name, lvl_sel, prev_game, prev_difficulty) # call the "repeat_menu" function with the same arguments

        if repeat.lower().startswith('y'):# check if the user input starts with 'y' ( to play the same game again)
            if prev_game is None or prev_difficulty is None: # check if there is a previous game and difficulty level
                print("There is no previous game to play again. Please choose another game.") # if there is no game will print this message
                repeat_menu(user_name, lvl_sel)  # if the prev_game and prev_difficulty = None than it will call the repreat_menu funtion from Replay module
            else:
                game_function = getattr(importlib.import_module('Games.' + prev_game), 'play') # get the game function from the module using "getattr" and "importlib" functions
                game_function(prev_difficulty) # call the game function with the previous difficulty level if the user will press y

        elif repeat.lower().startswith('n'): # check if the user input starts with 'n' (choose another game)
            Screen_cleaner() # clear the screen again
            # transfer_and_clear_file("./Scores/Scores.txt", "./Scores/Last_scores.txt") # for when the user will choose n for another game the function for clear the scores will be called and will also save the score to another file for the flask app localhost/last_score
            Livetests.load_game(user_name) # this will call the function load_game from the Livetests module to start another game from the beginning

        elif repeat.lower().startswith('q'):  # check if the user input starts with 'q' to quit the game
            print(f"Was nice to see you {user_name}!!! Thanks for playing my game, see you next time!") #will display a message at the end
            transfer_and_clear_file("./Scores/Scores.txt", "./Scores/Last_scores.txt") # calling the scores clean and transfer function
            Screen_cleaner() # clear the screen
            exit()   # will exit the program

        else:
            print("Invalid input, try again!")  #if the user will enter some other key except the allowed ones will be prompted to try again
            break   # this break will restart the loop

    # If the user chooses to play again, save the current game and difficulty level
    if repeat.lower().startswith('y'):
        prev_game = Livetests.game_to_load
        prev_difficulty = lvl_sel

    # Call the repeat_menu function again with the updated game and difficulty level
    repeat_menu(user_name, lvl_sel, prev_game, prev_difficulty)
