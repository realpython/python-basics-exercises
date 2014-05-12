# 4.2 review exercises


# Display the number of letters in the string
myWord = "antidisestablishmentarianism"
print(len(myWord))

# Concatenate two strings together
stringLeft = "bat"
stringRight = "man"
print(stringLeft + stringRight)

# Display two strings together, with a space in between
stringOne = "heebie"
stringTwo = "jeebies"
print(stringOne, stringTwo)


# Use subscripting to display part of a string
print("bazinga"[2:6])


# A more advanced way to do the above example would be:
myString = "bazinga"
startIndex = 2
print(myString[startIndex:len(myString)-startIndex+1])
