# 8.9 - Challenge: Simulate a Coin Toss Experiement
# Alternative solution to challenge


# Simulate the results of a series of coin tosses and track the results

# This one is tricky to structure correctly. Try writing out the logic before
# you start coding. Some additional pointers if you're stuck:
# 1. You will need to use a `for` loop over a range of trials.
# 2. For each trial, first you should check the outcome of the first flip.
# 3. Make sure you add the first flip to the total number of flips.
# 4. After the first toss, you'll need another loop to keep flipping while you
#    get the same result as the first flip.

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
