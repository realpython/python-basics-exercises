# 8.9 - Challenge: Simulate an Election
# Alternate solution to challenge


# Simulate the results of an election using a Monte Carlo simulation

from random import random


def run_regional_election(chance_A_wins):
    """Return the result of a regional election, either "A" or "B".

    The chances of "A" winning are determined by chance_A_wins.
    """
    if random() < chance_A_wins:
        return "A"
    else:
        return "B"


def run_election(regional_chances):
    """Return the result of an election, either "A" or "B".

    regional_chances is a list or tuple of floats representing the
    chances that candidate "A" will win in each region.

    For example, run_election([.2, .5, .7]) will run an election with
    three regions, where candidate "A" has a 20% chance to win in the
    first region, 50% in the second, and 70% in the third.
    """
    num_regions_won_by_A = 0
    for chance_A_wins in regional_chances:
        if run_regional_election(chance_A_wins) == "A":
            num_regions_won_by_A = num_regions_won_by_A + 1

    # Return the results. Note that the number of regions won by candidate
    # "B" is the total number of regions minus the number of regions won by
    # candidate "A". The total number of regions is the same as the length
    # of the regional_chances list.
    num_regions_won_by_B = len(regional_chances) - num_regions_won_by_A
    if num_regions_won_by_A > num_regions_won_by_B:
        return "A"
    else:
        return "B"


CHANCES_A_WINS_BY_REGION = [0.87, 0.65, 0.17]
NUM_TRIALS = 10_000

# Run the Monte-Carlo simulation
num_times_A_wins = 0
for trial in range(NUM_TRIALS):
    if run_election(CHANCES_A_WINS_BY_REGION) == "A":
        num_times_A_wins = num_times_A_wins + 1

# Display the probabilities that candidate A or candidate B wins the
# election. Note the probability that B wins can be calculated by
# subtracting the probability that A wins from 1.
print(f"Probability A wins: {num_times_A_wins / NUM_TRIALS}")
print(f"Probability B wins: {1 - (num_times_A_wins / NUM_TRIALS)}")
