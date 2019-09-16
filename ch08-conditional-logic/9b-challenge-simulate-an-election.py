# 8.9 - Challenge: Simulate an Election
# Solution to challenge


# Simulate the results of an election using a Monte Carlo simulation

from random import random

def wins_region(prob):
    if random() < prob:
        return 1
    else:
        return 0

def wins_election():
    return wins_region(.87) + wins_region(.65) + wins_region(.17) >= 2

wins = 0
for i in range(10_000):
    if wins_election():
        wins = wins + 1

print(f"% of elections won by 'Candidate A': {wins / 10_000:.2%}")
