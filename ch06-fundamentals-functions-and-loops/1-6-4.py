# 1.6.4 - Assignment: Convert temperatures
# Solution to assignment


# Convert Celsius and Fahrenheit temperatures using functions

def convert_cel_to_far(cel_temp):
    far_temp = cel_temp * 9 / 5 + 32
    return far_temp


def convert_far_to_cel(far_temp):
    cel_temp = (far_temp - 32) * 5 / 9
    return cel_temp


temp1 = 72
print("{} degrees F = {} degrees C".format(temp1, convert_far_to_cel(temp1)))

temp2 = 37
print("{} degrees C = {} degrees F".format(temp2, convert_cel_to_far(temp2)))
