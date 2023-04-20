import random  # import the "random" module
from Utils import Screen_cleaner  # import the "Screen_cleaner" function from the "Utils" module
from Scores.Score import add_score  # import the "add_score" function from the "Score" module

# define a function to generate a random sequence of numbers
def generate_sequence(lvl_sel):
    # create a list of "lvl_sel" random numbers between 1 and 101 (inclusive)
    secret_sequence = [random.randint(1, 101) for _ in range(int(lvl_sel))]
    return secret_sequence

# define a function to get a list of numbers from the user
def get_list_from_user(lvl_sel):
    user_input = input("Please enter {} numbers separated by spaces:   ".format(lvl_sel))  # prompt the user to enter a list of numbers
    # convert the user input to a list of integers (ignoring any non-digit characters)
    user_list = [int(num) for num in user_input.split() if num.isdigit()]
    while len(user_list) != lvl_sel:  # check if the length of the user's list is equal to "lvl_sel"
        print("Invalid input. Please enter {} numbers separated by spaces.".format(lvl_sel))  # display an error message
        user_input = input("Please enter {} numbers separated by spaces:   ".format(lvl_sel))  # prompt the user to enter a valid list of numbers
        user_list = [int(num) for num in user_input.split() if num.isdigit()]  # convert the user input to a list of integers
    return user_list

# define a function to check if two lists are equal
def is_list_equal(secret_sequence, user_list):
    if secret_sequence == user_list:  # check if the two lists are equal
        return True  # return True if the two lists are equal
    else:
        return False  # return False if the two lists are not equal

# define a function to play the game
def play(lvl_sel):
    secret_sequence = generate_sequence(lvl_sel)  # generate a secret sequence of numbers
    print(secret_sequence)  # print the secret sequence (for debugging purposes)

    Screen_cleaner()  # clear the screen using the "Screen_cleaner" function

    result = is_list_equal(secret_sequence, get_list_from_user(lvl_sel))  # get the user's list and check if it matches the secret sequence
    if result:  # if the user's list matches the secret sequence
        print("CONGRATULATIONS !!! Your TOTAL SCORE is: {}".format(add_score(lvl_sel)))  # display a congratulatory message and add the score to the score file
        return True  # return True (game won)
    else:  # if the user's list does not match the secret sequence
        print("BETTER LUCK NEXT TIME !!! The numbers were {} \n".format(secret_sequence))  # display a message showing the secret sequence
        return False  # return False (game lost)
