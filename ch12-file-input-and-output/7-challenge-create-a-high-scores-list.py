# 12.7 Challenge: Create a High Scores List
# Solution to Challenge

import csv
from pathlib import Path

# Change the path below to match the location on your computer
scores_csv_path = (
    Path.cwd()
    / "practice_files"
    / "scores.csv"
)

with scores_csv_path.open(mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    scores = [row for row in reader]

high_scores = {}
for item in scores:
    name = item["name"]
    score = int(item["score"])
    # If the name has not been added to the high_score dictionary, then
    # create a new key with the name and set its value to the score
    if name not in high_scores:
        high_scores[name] = score
    # Otherwise, check to see if score is greater than the score currently
    # assigned to high_scores[name] and replace it if it is
    else:
        if score > high_scores[name]:
            high_scores[name] = score

# The high_scores dictionary now contains one key for each name that was
# in the scores.csv file, and each value is that player's highest score.

output_csv_file = Path.cwd() / "high_scores.csv"
with output_csv_file.open(mode="w", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "high_score"])
    writer.writeheader()
    for name in high_scores:
        row_dict = {"name": name, "high_score": high_scores[name]}
        writer.writerow(row_dict)
