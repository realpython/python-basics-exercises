# 9.6 - Recover From Errors
# Solution to review exercises


# Ask the user to enter an integer.
# Repeat the process if the user hasn't entered an integer.
repeat = True
while repeat:
    try:
        my_input = input("Type an integer: ")
        print(int(my_input))
        repeat = False
    except ValueError:
        print("try again")
