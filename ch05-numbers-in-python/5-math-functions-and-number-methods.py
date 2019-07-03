# 5.5 - Math Functions and Number Methods
# Solutions to Review Exercises


# Exercise 1
user_input = input("Enter a number: ")
num = float(user_input)
print(f"{num} rounded to 2 decimal places is {round(num, 2)}")

# Exercise 2
user_input = input("Enter a number: ")
num = float(user_input)
print(f"The absolute value of {num} is {abs(num)}")

# Exercise 3
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
print(
    f"The difference between {num1} and {num2} is an integer? "
    f"{(num1 - num2).is_integer()}!"
)
