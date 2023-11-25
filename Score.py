from Utils import *


def add_score(difficulty):

    difficulty = int(difficulty)

    score_file = open(SCORES_FILE_NAME, 'r')

    current_score = int(score_file.read())

    score_file.close()

    score_file = open(SCORES_FILE_NAME, 'w')

    new_score = current_score + ((difficulty * 3) + 5)

    score_file.write(str(new_score))

    score_file.close()

