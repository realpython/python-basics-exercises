# 8.8 - Challenge: Simulate a Coin Toss Experiment
# Solution to challenge


# Simulate the results of a series of coin tosses and track the results

# This one is tricky to structure correctly. Try writing out the logic before
# you start coding. Some additional pointers if you're stuck:
# 1. You will need to use a `for` loop over a range of trials.
# 2. For each trial, first you should check the outcome of the first flip.
# 3. Make sure you add the first flip to the total number of flips.
# 4. After the first toss, you'll need another loop to keep flipping while you
#    get the same result as the first flip.

import random


def coin_flip():
    """Randomly return 'heads' or 'tails'."""
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"


flips = 0
num_trials = 10_000

for trial in range(num_trials):
    if coin_flip() == "heads":
        # Increment the number of flips by 1
        flips = flips + 1
        while coin_flip() == "heads":
            # Keep incrementing the total number of flips
            # until "tails" is returned by coin_flip()
            flips = flips + 1
        # Once coin_flip() return "tails", the loop will exit,
        # but we need to add one more to flips to track the
        # last flip that generated "tails"
        flips = flips + 1
    else:
        # coin_flip() returned "tails" on the first flip.
        # Increment the number of flips by 1
        flips = flips + 1
        while coin_flip() == "tails":
            # Keep incrementing the total number of flips
            # until "heads" is returned by coin_flip()
            flips = flips + 1
        # Once coin_flip() returns "heads", the loop will exit,
        # but we need to add one more to flips to track the
        # last flip that generated "heads"
        flips = flips + 1

avg_flips_per_trial = flips / num_trials
print(f"The average number of flips per trial is {avg_flips_per_trial}.")
