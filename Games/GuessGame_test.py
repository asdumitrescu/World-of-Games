# First, we import the necessary modules
import random
from Scores.Score import add_score

# Define a function named "generate_number" that takes a single argument, lvl_sel
# The function generates a random number between 1 and lvl_sel and returns it
def generate_number(lvl_sel):
    secret_number = random.randint(1, lvl_sel)
    return secret_number

# Define a function named "get_guess_from_user" that takes a single argument, lvl_sel
# The function prompts the user to enter a number between 1 and lvl_sel
# It returns the number entered by the user if it is valid
# If the input is invalid, the function will display an error message and prompt the user again
def get_guess_from_user(lvl_sel):
    while True:
        number = input(f"Please choose number between 1 to {lvl_sel}: ")
        if number.isdigit() and int(number) >= 1 and int(number) <= lvl_sel:
            return int(number)
        else:
            print("Invalid input, please enter a number between 1 to", lvl_sel)

# Define a function named "compare_results" that takes two arguments, number and secret_number
# The function compares the two numbers and returns True if they are equal, False otherwise
def compare_results(number, secret_number):
    if number == secret_number:
        return True
    else:
        return False

# Define a function named "play" that takes a single argument, lvl_sel
# The function calls the "generate_number" function to get a secret number
# It then prompts the user to enter a guess using the "get_guess_from_user" function
# The function compares the user's guess with the secret number using the "compare_results" function
# If the user's guess is correct, the function adds the score to the score file using the "add_score" function and returns True
# If the user's guess is incorrect, the function displays a message with the secret number and returns False
def play(lvl_sel):
    secret_number = generate_number(lvl_sel)

    number = int(get_guess_from_user(lvl_sel))

    result = compare_results(number, secret_number)

    if result:
        print("CONGRATULATIONS !!! Your TOTAL SCORE is: {}".format(add_score(lvl_sel)))
        return True
    else:
        print("BETTER LUCK NEXT TIME !!!")
        print(f'The number was: {secret_number}')
        print('\n')
        return False
