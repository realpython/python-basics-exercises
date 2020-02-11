# 12.5 Read and Write CSV Data
# Solutions to Exercises


# Exercise 1
import csv
from pathlib import Path

numbers = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]

file_path = Path.home() / "numbers.csv"

with file_path.open(mode="w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(numbers)


# Exercise 2
numbers = []

with file_path.open(mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        int_row = [int(num) for num in row]
        numbers.append(int_row)

print(numbers)


# Exercise 3
favorite_colors = [
    {"name": "Joe", "favorite_color": "blue"},
    {"name": "Anne", "favorite_color": "green"},
    {"name": "Bailey", "favorite_color": "red"},
]

file_path = Path.home() / "favorite_colors.csv"

with file_path.open(mode="w", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "favorite_color"])
    writer.writeheader()
    writer.writerows(favorite_colors)


# Exercise 4
favorite_colors = []

with file_path.open(mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        favorite_colors.append(row)

print(favorite_colors)
