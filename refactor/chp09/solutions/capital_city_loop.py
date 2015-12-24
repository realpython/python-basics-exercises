from capitals import capitals_dict
import random


def capital_game(state, capital):
    while True:
        guess = input("What is the capital of '{}'? ".format(state)).lower()
        if guess == "exit":
            print("The capital of '{}' is '{}'.".format(state, capital))
            print("Goodbye")
            break
        elif guess == (capital).lower():
            print("Correct! Nice job.")
            break


state = random.choice(list(capitals_dict.keys()))
capital = capitals_dict[state]
capital_game(state, capital)
