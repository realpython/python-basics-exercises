# chapter 7 election.py
# Simulate the results of an election using a Monte Carlo simulation

from random import random

total_A_wins = 0
total_B_wins = 0

trials = 100000
for trial in range(0, trials):
    A_win = 0
    B_win = 0
    if random() < .87:  # 1st region
        A_win += 1
    else:
        B_win += 1
    if random() < .65:  # 2nd region
        A_win += 1
    else:
        B_win += 1
    if random() < .17:  # 3rd region
        A_win += 1
    else:
        B_win += 1
    # determine overall election outcome
    if A_win > B_win:
        total_A_wins += 1
    else:
        total_B_wins += 1

print("Probability A wins:", total_A_wins / trials)
print("Probability B wins:", total_B_wins / trials)
