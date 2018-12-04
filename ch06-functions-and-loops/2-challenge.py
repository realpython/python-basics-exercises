# 6.2 - Challenge: Convert temperatures
# Solution to challenge


# Convert Celsius and Fahrenheit temperatures using functions


def convert_cel_to_far(cel_temp):
    far_temp = cel_temp * 9 / 5 + 32
    return far_temp


def convert_far_to_cel(far_temp):
    cel_temp = (far_temp - 32) * 5 / 9
    return cel_temp


temp1 = 72
print(f"{temp1} degrees F = {convert_far_to_cel(temp1)} degrees C")

temp2 = 37
print(f"{temp2} degrees C = {convert_cel_to_far(temp2)} degrees F")
