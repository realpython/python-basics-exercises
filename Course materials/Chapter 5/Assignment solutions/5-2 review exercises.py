# 5.2 review exercises

weight = 0.2
animal = "newt"

# Concatenate a number and a string in one print statement
print str(weight) + " kg is the weight of the newt."

# Use format() to print a number and a string inside of another string
print "{} kg is the weight of the {}.".format(weight, animal)

# Use format() to add objects inside a string using index numbers
# (Here we reversed the arguments - just because we could.)
print "{1} kg is the weight of the {0}.".format(animal, weight)

# Use format() to print new objects inside a string
print "{} kg is the weight of the {}.".format(0.2, "newt")

