# 8.3 - Control the Flow of Your Program
# Solutions to review exercises


# Exercise 1
# Display whether the length of user input is <, > or = 5 characters

my_input = input("Type something: ")

if len(my_input) < 5:
    print("Your input is less than 5 characters long.")
elif len(my_input) > 5:
    print("Your input is greater than 5 characters long.")
else:
    print("Your input is 5 characters long.")


# Exercise 2
# Number guessing program ("guess" the number 3)

print("I'm thinking of a number between 1 and 10. Guess which one.")
my_guess = input("Type in your guess: ")

if my_guess == "3":
    print("You win!")
else:
    print("You lose.")
