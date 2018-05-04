# 1.6.1 - Assignment: Perform Calculations on User Input
# Solution to Assignment


# Receive two input numbers and calculate their power

base = input("Enter a base: ")
exponent = input("Enter an exponent: ")
result = float(base) ** float(exponent)
print("{} to the power of {} = {}".format(base, exponent, result))
