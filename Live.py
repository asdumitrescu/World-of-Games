from Utils import transfer_and_clear_file, SCORES_FILE_NAME


def welcome():
    user_name = input("Please enter your name: ")

    with open('name.txt', 'w') as name_file:
        name_file.write(user_name)

    print('\n')

    print('''Hello {} and welcome to the World of Games (WoG).
Here you can find many cool games to play.\n'''.format(user_name))
    return user_name


from Scores.Score import add_score
from Games.CurrencyRoulette_test import play

def load_game(user_name):
    while True:
        while True:
            game_sel = input("""Please choose a game from the list by WRITING THE NUMBER then PUSH ENTER key:
==============================================================================
             1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
             ==============================================================================================
             2. Guess Game - guess a number and see if you chose like the computer. 
             =======================================================================
             3. Currency Roulette - try and guess the value between an interval of a random amount of USD in ILS for 
             the next mathemathic calcul:
             
             random number * USD in ILS  - (5 - Selected Difficulty), random number * USD in ILS + (5 - Selected Difficulty).
             ================================================================================================================
   >>> YOUR ANSWER HERE >>>:   """)

            while game_sel < '1' or game_sel > '3':
                print('Oooops Wrong INPUT! Please try entering again numbers from 1 to 3')
                game_sel = input("""Please choose a game from the list by WRITING THE NUMBER then PUSH ENTER key:
==================================================================================
             1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
             ==============================================================================================
             2. Guess Game - guess a number and see if you chose like the computer. 
             =======================================================================
             3. Currency Roulette - try and guess the value between an interval of a random amount of USD in ILS for 
             the next mathemathic calcul:
              
             random number * USD in ILS  - (5 - Selected Difficulty), random number * USD in ILS + (5 - Selected Difficulty).
             ================================================================================================================
   >>> YOUR ANSWER HERE >>>:   """)

            print('\n')

            if game_sel == '1':
                print('You Chose 1. Memory Game [GOOD LUCK!!!]\n')
            elif game_sel == '2':
                print('You Chose 2. Guess Game [GOOD LUCK!!!]\n')
            elif game_sel == '3':
                print('You chose 3. Currency Roulette [GOOD LUCK!!!]\n')
            else:
                print('\n')
            if game_sel.isdigit():
                break
        game_sel = int(game_sel)

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

            while lvl_sel < '1' or lvl_sel > '5':
                print('Oooops Wrong INPUT! Please try entering again numbers from 1 to 5')
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

            if lvl_sel == '1':
                print('Difficulty level', lvl_sel, 'selected! VERY EASY\n')
                break
            elif lvl_sel == '2':
                print('Difficulty level', lvl_sel, 'selected! EASY\n')
                break
            elif lvl_sel == '3':
                print('Difficulty level', lvl_sel, 'selected! MEDIUM\n')
                break
            elif lvl_sel == '4':
                print('Difficulty level', lvl_sel, 'selected! HARD\n')
                break
            elif lvl_sel == '5':
                print('Difficulty level', lvl_sel, 'selected! VERY HARD\n')

            if lvl_sel.isdigit():
                break
            else:
                print('\n')
        lvl_sel = int(lvl_sel)

        if game_sel == 1:
            # from Games.MemoryGame_test import play
            # from Scores.Score import add_score

            game = play(lvl_sel)

            if game:
                add_score(lvl_sel)

            while True:
                repeat = input("""Do you want to PLAY AGAIN the SAME GAME with the SAME DIFFICULTY, 
                OR you want to PLAY ANOTHER GAME?

                                To CONTINUE PLAYING the SAME GAME     
                          with the SAME DIFFICULTY please type in >>>:   Y.
                                                                  =========      
                                To Choose ANOTHER GAME please type in:   N.  
                                                              =============
                                If you want to EXIT please type in:      Q. 
                                                           ================                  
                >>> YOUR ANSWER HERE >>>:  """)

                print('\n')

                if repeat.startswith('Y') or repeat.startswith('y'):
                    game = play(lvl_sel)
                    if game:
                        add_score(lvl_sel)
                elif repeat.startswith('N') or repeat.startswith('n'):
                    break
                elif repeat.startswith('Q') or repeat.startswith('q'):
                    print(f"Was nice to see you {user_name}!!! Thanks for playing my game, see you next time !")
                    transfer_and_clear_file(SCORES_FILE_NAME, 'Scores/last_scores.txt')
                    exit()
                else:
                    print("Invalid input, try again!")

        elif game_sel == 2:
            # from Games.GuessGame_test import play
            # from Scores.Score import add_score

            game = play(lvl_sel)
            if game:
                add_score(lvl_sel)

            while True:
                repeat = input("""Do you want to PLAY AGAIN the SAME GAME with the SAME DIFFICULTY, 
                                OR you want to PLAY ANOTHER GAME?

                                                To CONTINUE PLAYING the SAME GAME     
                                          with the SAME DIFFICULTY please type in >>>:   Y.
                                                                                  =========      
                                                To Choose ANOTHER GAME please type in:   N.  
                                                                              =============
                                                If you want to EXIT please type in:      Q. 
                                                                           ================                  
                                >>> YOUR ANSWER HERE >>>:  """)

                print('\n')

                if repeat.startswith('Y') or repeat.startswith('y'):
                    game = play(lvl_sel)
                    if game:
                        add_score(lvl_sel)
                elif repeat.startswith('N') or repeat.startswith('n'):
                    break
                elif repeat.startswith('Q') or repeat.startswith('q'):
                    print(f"Was nice to see you {user_name}!!! Thanks for playing my game, see you next time !")
                    transfer_and_clear_file(SCORES_FILE_NAME, 'Scores/last_scores.txt')
                    exit()
                else:
                    print("Invalid input, try again!")

        elif game_sel == 3:
            # from Scores.Score import add_score
            # from Games.CurrencyRoulette_test import play

            game = play(lvl_sel)
            if game:
                add_score(lvl_sel)

            while True:
                repeat = input("""Do you want to PLAY AGAIN the SAME GAME with the SAME DIFFICULTY, 
                                 OR you want to PLAY ANOTHER GAME?

                                                To CONTINUE PLAYING the SAME GAME     
                                          with the SAME DIFFICULTY please type in >>>:   Y.
                                                                                  =========      
                                                To Choose ANOTHER GAME please type in:   N.  
                                                                              =============
                                                If you want to EXIT please type in:      Q. 
                                                                           ================                  
                                 >>> YOUR ANSWER HERE >>>:  """)

                print('\n')

                if repeat.startswith('Y') or repeat.startswith('y'):
                    game = play(lvl_sel)
                    if game:
                        add_score(lvl_sel)
                elif repeat.startswith('N') or repeat.startswith('n'):
                    break
                elif repeat.startswith('Q') or repeat.startswith('q'):
                    print(f"Was nice to see you {user_name}!!! Thanks for playing my game, see you next time !")
                    transfer_and_clear_file(SCORES_FILE_NAME, 'Scores/last_scores.txt')
                    exit()
                else:
                    print("Invalid input, try again!")
        else:
            print("Wrong choice, Try again!")
            load_game(user_name)
