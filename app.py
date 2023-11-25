import guess_game
import memory_game
import currency_roulette_game
from Score import *

def win_or_loss(result):
    if result:
        print("You Won!")
    else:
        print("You Lost!")

def welcome():
    while True:
        username = input("Welcome to WOG! Please Enter A Username:")
        if not username == "":
            print(f"Hi {username} and welcome to the World of Games: The Epic Journey")
            break
        else:
            print("You did not enter a Username")


def start_play():
    catalog = {1: "Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.",
               2: "Guess Game - guess a number and see if you chose like the computer.",
               3: "Currency Roulette - try and guess the value of a random amount of USD in ILS"}

    print("Games Catalog:")
    for option in catalog:
        print(option, catalog[option])

    while True:
        game = input("Please select a game to play by it's number:")
        if not game.isdecimal():
            print("Invalid input. Please enter a valid number.")
        else:
            game = int(game)
            if game in range(1, 4):
                break
            else:
                print("Please enter a number between 1 and 3.")

    print(f"""
    You have selected the game:
    {catalog[game]}
    """)

    while True:
        difficulty = input("Please choose a the game difficulty from 1 to 5 :")
        if not difficulty.isdecimal():
            print("Invalid input. Please enter a valid number.")
        else:
            difficulty = int(difficulty)
            if difficulty in range(1, 6):
                break
            else:
                print("Please enter a number between 1 and 5.")

    print(f"you have selected difficulty: {difficulty}")

    game_functions = {
        1: memory_game.play,
        2: guess_game.play,
        3: currency_roulette_game.play
    }

    result = game_functions[game](difficulty)
    win_or_loss(result)
    if result:
        add_score(difficulty)




