# 8.8 - Challenge: Simulate a Coin Toss Experiement
# Alternative solution to challenge


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
    # Flip the coin once and increment the flips tally by 1
    first_flip = coin_flip()
    flips = flips + 1
    # Continue flipping the coin and updating the tally until
    # a different result is returned by coin_flips()
    while coin_flip() == first_flip:
        flips = flips + 1
    # Increment the flip tally once more to account for the
    # final flip with a different result
    flips = flips + 1

avg_flips_per_trial = flips / num_trials
print(f"The average number of flips per trial is {avg_flips_per_trial}.")
