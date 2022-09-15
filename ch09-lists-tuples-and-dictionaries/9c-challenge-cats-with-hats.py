# 9.9 - Challenge: Cats With Hats
# Alternative solution to challenge using dictionaries


theCats = {}

# By default, no cats have been visited
# so we set every cat's number to False
for i in range(1, 101):
    theCats[i] = False

# Walk around the circle 100 times
for i in range(1, 101):
    # Visit all cats each time we do a lap
    for cats, hats in theCats.items():
        # Determine whether or not we visit a cat
        if cats % i == 0:
            # Add or remove the hat
            if theCats[cats]:
                theCats[cats] = False
            else:
                theCats[cats] = True

# Print whether each cat has a hat
for cats, hats in theCats.items():
    if theCats[cats]:
        print(f"Cat {cats} has a hat.")
    else:
        print(f"Cat {cats} is hatless!")
