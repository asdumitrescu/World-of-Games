from Livetests import load_game, welcome # importing the functions load_game and welcome from module Livetests

user_name = welcome() # calling the function welcome that will greet the user and get his name
                      # and we store it in a variable so the return value of welcome we use it in the load game function in this case will be the player name
load_game(user_name) # calling the load_game function to promt the menus for the game selections with the argument as the variable from the welcome function
