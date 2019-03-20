# 8.7 - Simulate Events and Calculate Probabilities
# Solutions to review exercises


from random import randint


# Exercise 1
# Write a function that simulatee the roll of a die.
def roll():
    """Return random integer between 1 and 6"""
    return randint(1, 6)


# Exercise 2
# Simulate 10,000 rolls of a die and display the average number rolled.
trials = 10000
total = 0

for trial in range(0, trials):
    total = total + roll()

avg_roll = total / trials

print(f"The average result of {trials} throws is {avg_roll}")
