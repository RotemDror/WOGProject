import random
import re
import time
from Utils import *


def generate_sequence(difficulty):

    number_list = []

    for number in range(1, (difficulty+1)):
        rand = random.randint(1, 101)
        number_list.append(rand)

    return number_list


def get_list_from_user(number_list):

    list_len = len(number_list)

    print(f"""In the following seconds- a list of {list_len} numbers in the range of 1-100 will be presented for 0.7 seconds.
    Your goal is to remember the entire set of numbers.
    """)

    time.sleep(5)

    stime = 5

    while stime:
        mins, secs = divmod(stime, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="")
        time.sleep(1)
        print("\r", end="")
        stime -= 1

    for number in number_list:
        print(number, end=" ")

    time.sleep(0.7)

    Screen_cleaner()

    users_answer = []

    answer_pattern = r'^\d+$'

    for number in range(1,list_len+1):

        while True:

            answer = input(f"Enter the {number} in the set of {list_len} numbers:")

            if not re.match(answer_pattern, answer):
                print("Invalid input. Please enter a valid number.")
            else:
                answer = int(answer)
                users_answer.append(answer)
                if answer not in range(1, 101):
                    print("Number out of scope")
                else:
                    break

    return users_answer


def is_list_equal(number_list, users_answer):

    final_answer = True

    for n in users_answer:
        if n not in number_list:
            final_answer = False

    return final_answer


def play(difficulty):

    number_list = generate_sequence(difficulty)
    users_answer = get_list_from_user(number_list)
    result = is_list_equal(number_list, users_answer)

    return result
