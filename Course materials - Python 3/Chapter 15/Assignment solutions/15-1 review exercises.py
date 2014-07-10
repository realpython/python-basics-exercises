# 15.1 review exercises

# Setup
import numpy


# Create a 3x3 array of the number 3 through 11 using reshape()
firstMatrix = numpy.arange(3, 12)
firstMatrix = firstMatrix.reshape(3, 3)

# Display the min, max and mean of all entries in the matrix
print "Min is", firstMatrix.min()
print "Max is", firstMatrix.max()
print "Mean is", firstMatrix.mean()

# Square every entry and save in a new matrix
secondMatrix = firstMatrix ** 2

# Put firstMatrix on top of secondMatrix
thirdMatrix = numpy.vstack([firstMatrix, secondMatrix])

# Calculate the dot product of thirdMatrix by firstMatrix
print numpy.dot(thirdMatrix, firstMatrix)

# Reshape thirdMatrix into a 3x3x2 matrix
thirdMatrix = thirdMatrix.reshape(3, 3, 2)
print thirdMatrix
