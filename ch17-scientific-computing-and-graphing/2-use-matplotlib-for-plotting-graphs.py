# 17.3 - Use matplotlib for Plotting Graphs
# Solution to review exercise #2

# Graph pirates versus global warming

from matplotlib import pyplot as plt
import csv
import os

# Change `path` to actual path on your system
path = "C:/Real Python/python-basics-exercises/ch16-scientific-computing-and-graphing/practice_files"

years = []
temperatures = []
pirates = []

with open(os.path.join(path, "pirates.csv"), "r") as my_file:
    my_file_reader = csv.reader(my_file)
    next(my_file_reader)  # skip header row
    for year, temperature, pirate_count in my_file_reader:
        years.append(int(year))
        temperatures.append(float(temperature))
        pirates.append(int(pirate_count))

plt.plot(pirates, temperatures, "r-o")

plt.title("Global temperature as a function of pirate population")
plt.xlabel("Total pirates")
plt.ylabel("Average global temperature (Celsius)")
plt.axis([-300, 48000, 14, 16])

# Annotate the plotted points with years.
for i in range(0, len(years)):
    plt.annotate(str(years[i]), xy=(pirates[i], temperatures[i]))

# Save and display graph.
plt.savefig(os.path.join(path, "Output/pirates.png"))
plt.show()
