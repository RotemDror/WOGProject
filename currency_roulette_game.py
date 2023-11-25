import requests
import random
import re
from Utils import *


def get_money_currency():

    url = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/ils.json"

    params = {"date": int, "ils": int}

    get_call = requests.get(url=url, params=params)

    data = get_call.json()

    ils = data["ils"]

    ils = "{:.2f}".format(ils)

    ils = float(ils)

    return ils


def get_guess_from_user():

    answer_pattern = r'^\d+$'

    random_dollars = random.randint(1, 100)

    while True:

        users_answer = input(f"How much are {random_dollars} USD in ILS? ")

        if not re.match(answer_pattern, users_answer):
            print("Invalid input. Please enter a valid number.")
        else:
            users_answer = int(users_answer)
            break

    answer_dict = {"users_answer": users_answer, "random_dollars": random_dollars}

    return answer_dict


def play(difficulty):

    mirror_difficulty = difficulty = 5 - difficulty

    currency = get_money_currency()

    users_return = get_guess_from_user()

    users_answer = users_return.get("users_answer")

    rand_dollar = users_return.get("random_dollars")

    true_answer = round(currency*rand_dollar)

    max_answer = true_answer + mirror_difficulty

    min_answer = true_answer - mirror_difficulty

    step = 1

    correct_answers = []

    current = min_answer

    while current <= max_answer:

        correct_answers.append(current)

        current = round(current + step, 2)

    if users_answer in correct_answers:
        return True
    else:
        return False



