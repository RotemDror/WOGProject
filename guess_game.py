import random
import re


def generate_number(difficulty):

    difficulty = difficulty+1

    secret_number = random.randint(1, difficulty)

    return secret_number


def get_guess_from_user(difficulty):

    answer_pattern = r'^\d+$'

    while True:

        users_answer = input(f"Try to guess the number i am thinking of: It is between 1 and {difficulty}:")

        if not re.match(answer_pattern, users_answer):
            print("Invalid input. Please enter a valid number.")
        else:
            users_answer = int(users_answer)
            range_difficulty = difficulty + 1
            if users_answer not in range(1, range_difficulty):
                print("Number out of scope")
            else:
                break

    return users_answer


def compare_results(secret_number, users_answer):

    if secret_number == users_answer:
        return True
    else:
        return False


def play(difficulty):

    secret_number = generate_number(difficulty)

    users_answer = get_guess_from_user(difficulty)

    results = compare_results(secret_number, users_answer)

    return results

