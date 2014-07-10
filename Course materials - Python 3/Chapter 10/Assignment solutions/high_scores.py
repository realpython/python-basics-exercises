 # 10.3 high_scores.py
 # Read in CSV data containing names and scores; display a high score list

import csv
import os
myPath = "C:/Real Python/Course materials/Chapter 10/Practice files"

highScoresDict = {}
with open(os.path.join(myPath, "scores.csv"), "rb") as myFile:
    myFileReader = csv.reader(myFile)
    for name, score in myFileReader:  # get each name/score pair
        score = int(score)  # convert string score to integer
        if name in highScoresDict:  # already had an entry for that name
            if score > highScoresDict[name]:  # new score is higher
                highScoresDict[name] = score
        else:  # haven't seen this name yet; add it to dictionary
            highScoresDict[name] = score

for name in sorted(highScoresDict):
    print name, highScoresDict[name]
