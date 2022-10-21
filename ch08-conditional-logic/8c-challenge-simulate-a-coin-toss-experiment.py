# 8.8 - Challenge: Simulate a Coin Toss Experiement
# Alternative solution to challenge using functions


# Simulate the results of a series of coin tosses and track the results

# This one is tricky to structure correctly. Try writing out the logic before
# you start coding. Some additional pointers if you're stuck:
# 1. You will need to use a `for` loop over a range of trials.
# 2. For each trial, first you should check the outcome of the first flip.
# 3. Make sure you add the first flip to the total number of flips.
# 4. After the first toss, you'll need another loop to keep flipping while you
#    get the same result as the first flip.

# Here is a simpler-to-read thus more pythonistic version, I think :P

import random

def coin_flip_trial():
    heads = 0
    tails = 0
    tries = 0
# As long as heads OR tails are zero, we have not had one of each.
    while heads == 0 or tails == 0:
        result = random.randint(0,1)
        tries = tries + 1
        if result == 1:
            heads = heads + 1
        else:
            tails = tails + 1
    return tries

# So let's now do that 10,000 times and then report the average number of trials it took.
tries_needed = 0
for x in range(10_000):
    tries_needed = tries_needed + coin_flip_trial()
    
print(f"It takes on average {tries_needed / 10_000:.2f} tries to get both a heads and a tails.")            


