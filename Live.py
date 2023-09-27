# We import the necessary functions from the modules 

from Scores.Score import add_score
from Utils import Screen_cleaner
from Replay import repeat_menu

import importlib


# We define a function to welcome the user

def welcome():
    # Prompt the user to enter their name
    user_name = input("Please enter your name: ")

    # Save the user's name to a file to be used for the flask app
    with open('name.txt', 'w') as name_file:
        name_file.write(user_name)

    print('\n')

    # Greet the user
    print('''Hello {} and welcome to the World of Games (WoG).
Here you can find many cool games to play.\n'''.format(user_name))
    return user_name

# We define a function to load the game menu and loop through game selections
def load_game(user_name):

    # Create a dictionary to map game selections to game modules and function names
    game_dict = {
        '1': ('MemoryGame', 'play', 'Memory Game'),
        '2': ('GuessGame', 'play', 'Guess Game'),
        '3': ('CurrencyRoulette', 'play', 'Currency Roulette')
    }
    prev_game = None
    prev_difficulty = None
    # Infinite loop
    while True:
        # Prompt the user to choose a game
        game_sel = input("""Please choose a game from the list by writing the number then pressing ENTER key:
        ==============================================================================
                 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
                 ==============================================================================================
                 2. Guess Game - guess a number and see if you chose like the computer. 
                 =======================================================================
                 3. Currency Roulette - try and guess the value between an interval of a random amount of USD in ILS for 
                 the next mathemathic calculation:

                 random number * USD in ILS  - (5 - Selected Difficulty), random number * USD in ILS + (5 - Selected Difficulty).
                 ================================================================================================================
        >>> YOUR ANSWER HERE >>>:   """)

        # We check if the user's selection is in the game dictionary
        if game_sel in game_dict:

            # We give variables to all the items inside the dictionary, eg.: game_module = 'MemoryGame_test' and so on.
            game_module, game_function, game_name = game_dict[game_sel]

            # Dynamically import the game module and function using importlib
            # So, in the load_game function, the program builds the name of the game module based on user selection
            # from game menu, and this is the part where all the users selection will import the desired function
            # in our case the function "play" from the actual game module, and will be used to play the game.
            game_function = getattr(importlib.import_module('Games.' + game_module), game_function)


            print(f"\nYou chose {game_name}! GOOD LUCK!!!\n")
            # Promt the user to select the difficulty level.
            while True:
                lvl_sel = input("""Please choose game difficulty from 1 to 5:   
            1 - VERY EASY
            ================
            2 -   EASY
            ================
            3 -  MEDIUM
            ================
            4 -   HARD
            ================
            5 - VERY HARD
            ================
            >>> YOUR ANSWER HERE >>>:   """)

            # Check if user input is a digit and within range of 1 to 5
                if lvl_sel.isdigit() and '1' <= lvl_sel <= '5':
                    # Casting / converting from str to int (as you told me ), and print selected difficulty level
                    lvl_sel = int(lvl_sel)
                    print(f"Difficulty level {lvl_sel} selected!")

                    # Print the name of the difficulty for the user choice
                    if lvl_sel == 1:
                        print("VERY EASY\n")
                    elif lvl_sel == 2:
                        print("EASY\n")
                    elif lvl_sel == 3:
                        print("MEDIUM\n")
                    elif lvl_sel == 4:
                        print("HARD\n")
                    else:
                        print("VERY HARD\n")

                    break

                else:
                    print('Invalid input, try again numbers from 1 - 5')
                    Screen_cleaner()
                    continue

                    # The while loop to play the game
            while True:
                # Calling the function play from the selected module with the lvl of difficulty and start the game
                game = game_function(lvl_sel)

                # Since our function play is boolean when the user win the game, the function will return True
                # so if game == True: call the score function to add the score in a file
                # then the screen cleaner function to clean the screen and after that whatever next he gets
                # the repeat menu function imported from Utils file.
                if game:
                    add_score(lvl_sel)
                    Screen_cleaner()

                repeat_menu(user_name, lvl_sel, prev_game = game_module, prev_difficulty = lvl_sel)


             # The else block is the error handling section of the load_game function. It is executed when the user inputs a value that
             # is not in the game dictionary, i.e., not one of the options presented in the game menu.        
        else:
            print('Oooops Wrong INPUT! Please try entering again numbers from 1 to 3\n')
            Screen_cleaner()
