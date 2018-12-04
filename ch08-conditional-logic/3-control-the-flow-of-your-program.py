# 8.3 - Control the Flow of Your Program
# Solutions to review exercises


# Display whether the length of user input is <, > or = 5 characters

my_input = input("Type something: ")

if len(my_input) < 5:
    print("Your input is less than 5 characters long.")
elif len(my_input) > 5:
    print("Your input is greater than 5 characters long.")
else:
    print("Your input is 5 characters long.")
