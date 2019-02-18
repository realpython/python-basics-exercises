# 6.2 - Challenge: Convert temperatures
# Solution to challenge


def convert_cel_to_far(temp_cel):
    """Return the Celsius temperature temp_cel converted to Fahrenheit."""
    temp_far = temp_cel * (9 / 5) + 32
    return temp_far


def convert_far_to_cel(temp_far):
    """Return the Fahrenheit temperature temp_far converted to Celsius."""
    temp_cel = (temp_far - 32) * (5 / 9)
    return temp_cel


temp_far = input("Enter a temperature in degrees F: ")
temp_cel = convert_far_to_cel(float(temp_far))
print(f"{temp_far} degrees F = {temp_cel:.2f} degrees C")


temp_cel = input("\nEnter a temperature in degrees C: ")
temp_far = convert_cel_to_far(float(temp_cel))
print(f"{temp_cel} degrees C = {temp_far:.2f} degrees F")
