# 17.2 - Use matplotlib for Plotting Graphs
# Solution to review exercise #2

# Setup
import numpy as np


# Exercise 1
# Create a 3x3 array of the number 3 through 11 using reshape()
first_matrix = np.arange(3, 12).reshape(3, 3)

# Exercise 2
# Display the min, max and mean of all entries in the matrix
print(f"Min is {first_matrix.min()}")
print(f"Max is {first_matrix.max()}")
print(f"Mean is {first_matrix.mean()}")

# Exercise 3
# Square every entry and save in a new matrix
second_matrix = first_matrix**2

# Exercise 4
# Put first_matrix on top of second_matrix
third_matrix = np.vstack([first_matrix, second_matrix])

# Exercise 5
# Calculate the dot product of third_matrix by first_matrix
print(third_matrix @ first_matrix)

# Exercise 6
# Reshape third_matrix into a 3x3x2 matrix
third_matrix = third_matrix.reshape(3, 3, 2)
print(third_matrix)
