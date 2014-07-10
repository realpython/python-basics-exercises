# 10.1 review exercises


'''
In order to run correctly, this script first needs to
be placed in the Chapter 10 "Practice files" folder.
(File paths are covered in section 10.2)
'''

# Read a text file by looping over individual lines
myPoem = open("poem.txt", "r")
for line in myPoem.readlines():
    # Use a comma after the print statement;
    # file already contains newline characters
    print line,
myPoem.close()

# Print some blank lines to separate the two examples
print "\n\n"

# Use "with" to automatically close a file when finished
with open("poem.txt", "r") as myPoem:
    for line in myPoem.readlines():
        print line,

# Write the contents of one file into another, line-by-line
poemIn = open("poem.txt", "r")
poemOut = open("output.txt", "w")
for line in poemIn.readlines():
    poemOut.write(line)
poemIn.close()
poemOut.close()

# Repeat the previous exercise using the "with" keyword
# (This will overwrite the previous output file.)
with open("poem.txt", "r") as poemIn, open("output.txt", "w") as poemOut:
    for line in poemIn.readlines():
        poemOut.write(line)


# Append a new line to the end of "output.txt"
# (Need to start on a new line, so add "\n" to the beginning.)
with open("output.txt", "a") as poemAppend:
    poemAppend.write("\nThus ends the haiku.")
