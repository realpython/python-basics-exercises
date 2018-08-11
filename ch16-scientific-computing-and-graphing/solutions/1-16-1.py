# 1.15.1 - Use NumPy for Matrix Manipulation
# Solutions to review exercises

# Setup
import numpy


# Exercise 1
# Create a 3x3 array of the number 3 through 11 using reshape()
first_matrix = numpy.arange(3, 12)
first_matrix = first_matrix.reshape(3, 3)

# Exercise 2
# Display the min, max and mean of all entries in the matrix
print "Min is", first_matrix.min()
print "Max is", first_matrix.max()
print "Mean is", first_matrix.mean()

# Exercise 3
# Square every entry and save in a new matrix
second_matrix = first_matrix ** 2

# Exercise 4
# Put first_matrix on top of second_matrix
third_matrix = numpy.vstack([first_matrix, second_matrix])

# Exercise 5
# Calculate the dot product of third_matrix by first_matrix
print(numpy.dot(third_matrix, first_matrix))

# Exercise 6
# Reshape third_matrix into a 3x3x2 matrix
third_matrix = third_matrix.reshape(3, 3, 2)
print(third_matrix)
