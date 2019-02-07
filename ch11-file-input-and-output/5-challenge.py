# 11.5 - Challenge: Create a High Scores List From CSV Data
# Solution to challenge


# Read in CSV data containing names and scores; display a high score list

import csv
import os

# Change my_path to the correct path on your system
path = "C:/Real Python/python-basics-exercises/\
/ch11-file-input-and-output/practice_files"

high_scores_dict = {}
with open(os.path.join(path, "scores.csv"), "r") as myFile:
    my_file_reader = csv.reader(myFile)
    for name, score in my_file_reader:  # get each name/score pair
        score = int(score)  # convert string score to integer
        if name in high_scores_dict:  # already had an entry for that name
            if score > high_scores_dict[name]:  # new score is higher
                high_scores_dict[name] = score
        else:  # haven't seen this name yet; add it to dictionary
            high_scores_dict[name] = score

for name in sorted(high_scores_dict):
    print(name, high_scores_dict[name])
