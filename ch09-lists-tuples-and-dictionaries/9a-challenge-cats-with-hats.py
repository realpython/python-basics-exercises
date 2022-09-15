# 9.9 - Challenge: Cats With Hats
# Solution to challenge


def get_cats_with_hats(array_of_cats):
    cats_with_hats_on = []
    # We want to walk around the circle 100 times
    for num in range(1, 100 + 1):
        # Each time we walk around, we visit 100 cats
        for cat in range(1, 100 + 1):
            # Determine whether to visit the cat
            # Use modulo operator to visit every 2nd, 3rd, 4th,... etc.
            if cat % num == 0:
                # Remove or add hat depending on
                # whether the cat already has one
                if array_of_cats[cat] is True:
                    array_of_cats[cat] = False
                else:
                    array_of_cats[cat] = True

    # Add all number of each cat with a hat to list
    for cat in range(1, 100 + 1):
        if array_of_cats[cat] is True:
            cats_with_hats_on.append(cat)

    # Return the resulting list
    return cats_with_hats_on


# Cats contains whether each cat already has a hat on,
# by default all are set to false since none have been visited
cats = [False] * (100 + 1)
print(get_cats_with_hats(cats))
