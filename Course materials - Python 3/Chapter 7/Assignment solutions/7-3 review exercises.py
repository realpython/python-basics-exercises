# 7.3 review exercises


# Initial setup
import os
import csv
# This path may need to be changed depending on your setup
path = "C:/Real Python/Course Materials/Chapter 7/Practice files"


# Read in a CSV and display each row except the header row
# Append a third column and write out the resulting CSV with a new header
inFilePath = os.path.join(path, "pastimes.csv")
outFilePath = os.path.join(path, "Output/categorized pastimes.csv")
with open(inFilePath, "rb") as inFile, open(outFilePath, "wb") as outFile:
    csvReader = csv.reader(inFile)
    csvWriter = csv.writer(outFile)
    
    # skip header row and write a new output header row
    csvReader.next()
    csvWriter.writerow(["Name", "Favorite Pastime", "Type of pastime"])
    
    for row in csvReader:
        print row
        # Check if "Favorite Pastime" includes "fighting"
        if row[1].lower().find("fighting") != -1:
            row.append("Combat")
        else:
            row.append("Other")
        # Add the new row to the output
        csvWriter.writerow(row)

