# 6.6 - Work With Numbers
# Solutions to Review Exercises


# Exercise 1
num = float(input("Enter a number to be rounded to two decimal places: "))
print(f"{round(num, 2)}")

# Exercise 2
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
print(
    f"The difference between {num1} and {num2} is an integer?"
    f"{(num1 - num2).is_integer()}!"
)
