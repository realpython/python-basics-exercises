# 6.1 exponent.py
# Receive two input numbers and calculate their power

base = raw_input("Enter a base: ")
exponent = raw_input("Enter an exponent: ")
result = float(base) ** float(exponent)
print "{} to the power of {} = {}".format(base, exponent, result)
