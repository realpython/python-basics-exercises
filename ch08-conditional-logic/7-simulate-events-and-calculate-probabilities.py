# 8.7 - Simulate Events and Calculate Probabilities
# Solutions to review exercises


from random import randint


# Exercise 1
# Simulate the toss of a die
print(randint(1, 6))


# Exercise 2
# Simulate 10,000 throws of dice and display the average result
trials = 10000
total = 0
for trial in range(0, trials):
    total += randint(1, 6)
avg_result = total / trials
print(f"The average result of {trials} throws was {avg_result}")
