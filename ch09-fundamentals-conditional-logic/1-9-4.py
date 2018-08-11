# 1.9.4 - Assignment: Find the Factors of a Number
# Solution to assignment


# display all the factors of a number chosen by the user

num = int(input("Enter a positive integer: "))
for divisor in range(1, num + 1):
    if num % divisor == 0:
        print("{} is a divisor of {}".format(divisor, num))
