# 8.4 review exercises


# Run in an infinite loop until the user types "q" or "Q"
while True:
    my_input = raw_input('Type "q" or "Q" to quit: ')
    if my_input.upper() == "Q":
        break

# Display every number from 1 through 50 except multiples of 3
for i in range(1, 51):
    if i % 3 == 0:
        continue
    print i
