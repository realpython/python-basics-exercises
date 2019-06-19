# 8.6 - Recover From Errors
# Solution to review exercises


# Exercise 1
# Ask the user to enter an integer.
# Repeat the process if the user hasn't entered an integer.
while True:
    try:
        my_input = input("Type an integer: ")
        print(int(my_input))
        break
    except ValueError:
        print("try again")


# Exercise 2
# Print character and specifid index in string

input_string = input("Enter a string: ")

try:
    index = int(input("Enter an integer: "))
    print(input_string[index])
except ValueError:
    print("Invalid number")
except IndexError:
    print("Index is out of bounds")
