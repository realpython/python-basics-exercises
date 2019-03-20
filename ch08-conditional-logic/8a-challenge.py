# 8.9 - Challenge: Simulate a Coin Toss Experiment
# Solution to challenge


# Simulate the results of a series of coin tosses and track the results

# This one is tricky to structure correctly. Try writing out the logic before
# you start coding. Some additional pointers if you're stuck:
# 1. You will need to use a `for` loop over a range of trials.
# 2. For each trial, first you should check the outcome of the first flip.
# 3. Make sure you add the first flip to the total number of flips.
# 4. After the first toss, you'll need another loop to keep flipping while you
#    get the same result as the first flip.

from random import randint

flips = 0
trials = 10000

for trial in range(0, trials):
    flips += 1  # first flip
    if randint(0, 1) == 0:  # flipped tails on first flip
        while randint(0, 1) == 0:  # keep flipping tails
            flips += 1
        flips += 1  # finally flipped heads
    else:  # otherwise, flipped heads on first flip
        while randint(0, 1) == 1:  # keep flipping heads
            flips += 1
        flips += 1  # finally flipped tails

print(flips / trials)
