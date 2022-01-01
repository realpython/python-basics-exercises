# 9.9 - Challenge: Cats With Hats
# Solution to challenge


def get_cats_with_hats(array_of_cats):
    cats_with_hats_on = []
    for num in range(1, 100 + 1):
        for cat in range(1, 100 + 1):
            if cat % num == 0:
                if array_of_cats[cat] is True:
                    array_of_cats[cat] = False
                else:
                    array_of_cats[cat] = True
    for cat in range(1, 100 + 1):
        if cats[cat] is True:
            cats_with_hats_on.append(cat)
    return cats_with_hats_on


cats = [False] * (100 + 1)
print(get_cats_with_hats(cats))

## Alternate Solution

cats = {}

for i in range(1, 101):
    cats[i] = False

for i in range(1, 101):
    for j in range(i,101,i):
        cats[j] = not cats[j]

print("Cats having hats")

for i in cats:
    if cats[i]:
        print(f'Cat # {i} has a hat on')
