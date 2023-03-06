import random

from Utils import Screen_cleaner
from Scores.Score import add_score


def generate_sequence(lvl_sel):
    secret_sequence = [random.randint(1, 101) for _ in range(int(lvl_sel))]
    return secret_sequence


def get_list_from_user(lvl_sel):
    user_input = input("Please enter {} numbers separated by spaces:   ".format(lvl_sel))
    user_list = [int(num) for num in user_input.split() if num.isdigit()]
    while len(user_list) != lvl_sel:
        print("Invalid input. Please enter {} numbers separated by spaces.".format(lvl_sel))
        user_input = input("Please enter {} numbers separated by spaces:   ".format(lvl_sel))
        user_list = [int(num) for num in user_input.split() if num.isdigit()]
    return user_list


def is_list_equal(secret_sequence, user_list):
    if secret_sequence == user_list:
        return True
    else:
        return False


def play(lvl_sel):
    secret_sequence = generate_sequence(lvl_sel)
    print(secret_sequence)

    Screen_cleaner()

    result = is_list_equal(secret_sequence, get_list_from_user(lvl_sel))
    if result:
        print("CONGRATULATIONS !!! Your TOTAL SCORE is: {}".format(add_score(lvl_sel)))
        return True
    else:
        print("BETTER LUCK NEXT TIME !!! The numbers were {} \n".format(secret_sequence))
        return False
