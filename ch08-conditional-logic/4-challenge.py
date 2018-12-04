# 8.4 - Challenge: Find the Factors of a Number
# Solution to challenge


# Display all the factors of a number chosen by the user

num = int(input("Enter a positive integer: "))
for divisor in range(1, num + 1):
    if num % divisor == 0:
        print(f"{divisor} is a factor of {num}")
