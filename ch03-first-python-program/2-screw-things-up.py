# 3.2 - Screw Things Up
# Solutions to review exercies


# Exercise 1
# The following line won't run because of a syntax error
print("hi)

# We didn't close the double quotes at the end of the string.
# The line above needed to have been:
# print("hi")


# Exercise 2
''' The following lines won't run properly,
    even if the syntax error in the line above is corrected,
    because of a run-time error '''
print(hello)

# We meant to print the string "hello";
# a variable named 'hello' doesn't exist yet.
#
# This line could have been:
#
# my_string = "hello"
# print(my_string)
