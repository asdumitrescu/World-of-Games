import random

from currency_converter import CurrencyConverter

from Scores.Score import add_score


def get_money_interval(lvl_sel):
    c = CurrencyConverter()

    random_number = random.randint(1, 101)
    print(f'The random number is: {random_number} ')

    usd_v = c.convert(1, "USD", "ILS")
    print('The value of Dollar in Shekels:', usd_v)

    random_dollars = c.convert(random_number, "USD", "ILS")
    interval = (random_dollars - (5 - lvl_sel), random_dollars + (5 - lvl_sel))
    return interval


def get_guess_from_user():
    while True:
        user_input = input("""Enter a decimal number, for example 202.32 or 202.3, that is between the next interval:
             (random number * USD in ILS  - (5 - Selected Difficulty),random number * USD in ILS + (5 - Selected Difficulty)): """)
        if user_input.count(".") == 1 and user_input.replace(".", "").isdigit():
            return float(user_input)
        print("Invalid input. Please enter a valid decimal number.")


def play(lvl_sel):
    random_money = get_money_interval(lvl_sel)
    money_from_user = float(get_guess_from_user())

    if random_money[0] <= money_from_user <= random_money[1]:
        print("CONGRATULATIONS !!! YOUR TOTAL POINTS ARE {} !!!".format(add_score(lvl_sel)))
        return True
    else:

        print("BETTER LUCK NEXT TIME !!!")
        print('The interval was {}\n'.format(random_money))
        return False
