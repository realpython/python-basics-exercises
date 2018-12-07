# 8.9 - Challenge: Simulate a Coin Toss Experiement
# Alternative solution to challenge


# Simulate the results of a series of coin tosses and track the results

from random import randint


trials = 100_000
flips = 0

for trial in range(1, trials):
    first_flip = randint(0, 1)
    flips += 1
    while randint(0, 1) == first_flip:
        flips += 1
    flips += 1

print(f"The average number of coin flips was {flips / trials}")
