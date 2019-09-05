# 9.8 - Challenge: Cats With Hats
# Alternative solution to challenge using dictionaries


theCats = {}

for i in range(1, 101):
    theCats[i] = False

for i in range(1, 101):
    for cats, hats in theCats.items():
        if cats % i == 0:
            if theCats[cats]:
                theCats[cats] = False
            else:
                theCats[cats] = True

for cats, hats in theCats.items():
    if theCats[cats]:
        print(f"Cat {cats} has a hat.")
    else:
        print(f"Cat {cats} is hatless!")
