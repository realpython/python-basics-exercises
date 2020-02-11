# 12.5 - Reading and Writing Files
# Solutions to Exercises


# Exercise 1
from pathlib import Path

starships = ["Discovery\n", "Enterprise\n", "Defiant\n", "Voyager"]

file_path = Path.home() / "starships.txt"
with file_path.open(mode="w", encoding="utf-8") as file:
    file.writelines(starships)


# Exercise 2
with file_path.open(mode="r", encoding="utf-8") as file:
    for starship in file.readlines():
        print(starship, end="")


# Exercise 3
with file_path.open(mode="r", encoding="utf-8") as file:
    for starship in file.readlines():
        if starship.startswith("D"):
            print(starship, end="")
