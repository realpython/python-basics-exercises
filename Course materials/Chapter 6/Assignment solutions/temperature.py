# 6.2 temperature.py
# Convert Celsius and Fahrenheit temperatures using functions

from __future__ import division

def convertCtoF(celTemp):
    farTemp = celTemp * 9/5 + 32
    return farTemp

def convertFtoC(farTemp):
    celTemp = (farTemp - 32) * 5/9
    return celTemp

temp1 = 72
print "{} degrees F = {} degrees C".format(temp1, convertFtoC(temp1))

temp2 = 37
print "{} degrees C = {} degrees F".format(temp2, convertCtoF(temp2))
