# Import the necessary modules
import random
from currency_converter import CurrencyConverter
from Scores.Score import add_score


# Define a function that generates a random money interval based on the difficulty level
def get_money_interval(lvl_sel):
    # Create a new instance of the CurrencyConverter class
    c = CurrencyConverter()

    # Generate a random number between 1 and 101
    random_number = random.randint(1, 101)
    # Print the random number
    print(f'The random number is: {random_number} ')

    # Convert 1 USD to ILS and print the result
    usd_v = c.convert(1, "USD", "ILS")
    print('The value of Dollar in Shekels:', usd_v)

    # Convert the random number to ILS and create an interval based on the difficulty level
    random_dollars = c.convert(random_number, "USD", "ILS")
    interval = (random_dollars - (5 - lvl_sel), random_dollars + (5 - lvl_sel))
    return interval


# Define a function that gets a decimal number from the user
def get_guess_from_user():
    while True:
        # Prompt the user to enter a decimal number within the specified interval
        user_input = input("""Enter a decimal number, for example 202.32 or 202.3, that is between the next interval:
             (random number * USD in ILS  - (5 - Selected Difficulty),random number * USD in ILS + (5 - Selected Difficulty)): """)
        # Check if the user input is a valid decimal number
        if user_input.count(".") == 1 and user_input.replace(".", "").isdigit():
            return float(user_input)
        # If the input is invalid, prompt the user to enter a valid decimal number
        print("Invalid input. Please enter a valid decimal number.")


# Define a function that plays the game
def play(lvl_sel):
    # Get the random money interval based on the difficulty level
    random_money = get_money_interval(lvl_sel)
    # Get a decimal number from the user
    money_from_user = float(get_guess_from_user())

    # Check if the user's guess is within the random money interval
    if random_money[0] <= money_from_user <= random_money[1]:
        # If the guess is correct, add the score to the user's total score and print a message
        print("CONGRATULATIONS !!! YOUR TOTAL POINTS ARE {} !!!".format(add_score(lvl_sel)))
        return True
    else:
        # If the guess is incorrect, print a message with the correct interval and return False
        print("BETTER LUCK NEXT TIME !!!")
        print('The interval was {}\n'.format(random_money))
        return False
