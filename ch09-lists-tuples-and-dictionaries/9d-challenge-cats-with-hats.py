# 9.9 - Challenge: Cats With Hats
# Alternative solution to challenge(nested loops)

for i in range(1,101):
# Counting number of actions with hat
    count = 1
    for j in range(1, i):
        if i % j == 0:
            count += 1
# Determine what action was last
    if count % 2 == 1:
        print(f"Cat {i} has a hat.")