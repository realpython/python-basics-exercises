# 9.7 - Challenge: Capital City Loop
# Solution to challenge


from capitals import capitals_dict
import random


def capital_game(state, capital):
    while True:
        guess = input(f"What is the capital of '{state}'? ").lower()
        if guess == "exit":
            print(f"The capital of '{state}' is '{capital}'.")
            print("Goodbye")
            break
        elif guess == (capital).lower():
            print("Correct! Nice job.")
            break


state = random.choice(list(capitals_dict.keys()))
capital = capitals_dict[state]
capital_game(state, capital)
