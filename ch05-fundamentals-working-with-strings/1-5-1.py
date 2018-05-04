# 1.5.1 - Streamline Your Print Statements
# Solutions to review exercies


# Exercise 1
weight = 0.2
animal = "newt"

# Concatenate a number and a string in one print statement
print(str(weight) + " kg is the weight of the newt.")


# Exercise 2
# Use format() to print a number and a string inside of another string
print("{} kg is the weight of the {}.".format(weight, animal))


# Exercise 3
# Use format() to add objects inside a string using index numbers
# (Here we reversed the arguments - just because we could.)
print("{1} kg is the weight of the {0}.".format(animal, weight))


# Exercise 4
# Use format() to print new objects inside a string
print("{} kg is the weight of the {}.".format(0.2, "newt"))


# Exercise 5
# Use formatted string literal to reference objects inside a string
print(f"{weight} kg is the weight of the {animal}.")
