# Ch 11.2 - Working With Packages
# main.py - Solution to Exercise 2

from helpers.string import shout
from helpers.math import area


length = 5
width = 8
message = f"The area of a {length}-by-{width} rectangle is {area(length, width)}"
print(shout(message))
