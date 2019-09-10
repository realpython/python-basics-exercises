# 8.5 - Break Out of the Pattern
# Solutions to review exercises


# Exercise 1
# Run in an infinite loop until the user types "q" or "Q"
while True:
    user_input = input('Type "q" or "Q" to quit: ')
    if user_input.upper() == "Q":
        break


# Exercise 2
# Display every number from 1 through 50 except multiples of 3
for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)
