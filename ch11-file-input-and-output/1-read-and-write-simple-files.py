# 11.1 - Read and Write Simple Files
# Solutions to review exercises


"""
In order to run correctly, this script first needs to
be placed in the Chapter 10 "practice_files" folder.
(File paths are covered in section 10.2)
"""

# Read a text file by looping over individual lines
my_poem = open("poem.txt", "r")
for line in my_poem.readlines():
    # Replace automatic line break at end of line;
    # file already contains newline characters
    print(line, end="")
my_poem.close()

# Print some blank lines to separate the two examples
print("\n\n")

# Use "with" to automatically close a file when finished
with open("poem.txt", "r") as my_poem:
    for line in my_poem.readlines():
        print(line, end="")

# Write the contents of one file into another, line-by-line
poem_in = open("poem.txt", "r")
poem_out = open("output.txt", "w")
for line in poem_in.readlines():
    poem_out.write(line)
poem_in.close()
poem_out.close()

# Repeat the previous exercise using the "with" keyword
# (This will overwrite the previous output file.)
with open("poem.txt", "r") as poem_in, open("output.txt", "w") as poem_out:
    for line in poem_in.readlines():
        poem_out.write(line)


# Append a new line to the end of "output.txt"
# (Need to start on a new line, so add "\n" to the beginning.)
with open("output.txt", "a") as poem_append:
    poem_append.write("\nThus ends the haiku.")
