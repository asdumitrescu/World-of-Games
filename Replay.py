import importlib
import Livetests
from Utils import Screen_cleaner, transfer_and_clear_file, SCORES_FILE_NAME
def repeat_menu(user_name, lvl_sel, prev_game=None, prev_difficulty=None):
    while True:
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

        if repeat == "" or repeat not in ['y', 'n', 'q']:
            print('Invalid input, try again!')
            Screen_cleaner()
            repeat_menu(user_name, lvl_sel, prev_game, prev_difficulty)

        if repeat.lower().startswith('y'):
            if prev_game is None or prev_difficulty is None:
                print("There is no previous game to play again. Please choose another game.")
                repeat_menu(user_name, lvl_sel)
            else:
                game_function = getattr(importlib.import_module('Games.' + prev_game), 'play')
                game_function(prev_difficulty)

        elif repeat.lower().startswith('n'):
            Screen_cleaner()
            Livetests.load_game(user_name)

        elif repeat.lower().startswith('q'):
            print(f"Was nice to see you {user_name}!!! Thanks for playing my game, see you next time!")
            transfer_and_clear_file(SCORES_FILE_NAME, 'last_scores.txt')
            Screen_cleaner()
            exit()

        else:
            print("Invalid input, try again!")
            break

    # If the user chooses to play again, save the current game and difficulty level
    if repeat.lower().startswith('y'):
        prev_game = Livetests.game_to_load
        prev_difficulty = lvl_sel

    # Call the repeat_menu function again with the updated game and difficulty level
    repeat_menu(user_name, lvl_sel, prev_game, prev_difficulty)
