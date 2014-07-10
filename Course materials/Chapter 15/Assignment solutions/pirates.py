# 11.2 pirates.py
# Graph pirates versus global warming

from matplotlib import pyplot as plt
import csv
import os
path = "C:/Real Python/Course materials/Chapter 15/Practice files"

years = []
temperatures = []
pirates = []

with open(os.path.join(path, "pirates.csv"), "rb") as myFile:
    myFileReader = csv.reader(myFile)
    myFileReader.next()  # skip header row
    for year, temperature, pirateCount in myFileReader:
        years.append(year)
        temperatures.append(temperature)
        pirates.append(pirateCount)

plt.plot(pirates, temperatures, "r-o")

# label graph
plt.title("Global temperature as a function of pirate population")
plt.xlabel("Total pirates")
plt.ylabel("Average global temperature (Celsius)")
plt.axis([-300, 48000, 14, 16])

# annotate points with years
for i in range(0, len(years)):
    plt.annotate(str(years[i]), xy=(pirates[i], temperatures[i]))

# save and display graph
plt.savefig(os.path.join(path, "Output/pirates.png"))
plt.show()
