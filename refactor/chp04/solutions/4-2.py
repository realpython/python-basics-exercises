# 4.2 review exercises


# Display the number of letters in the string
my_word = "antidisestablishmentarianism"
print(len(my_word))

# Concatenate two strings together
string_left = "bat"
string_right = "man"
print(string_left + string_right)

# Display two strings together, with a space in between
string_one = "heebie"
string_two = "jeebies"
print(string_one, string_two)


# Use subscripting to display part of a string
print("bazinga"[2:6])


# A more advanced way to do the above example would be:
my_string = "bazinga"
start_index = 2
print(my_string[start_index:len(my_string) - start_index + 1])
