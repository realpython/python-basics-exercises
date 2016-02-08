# 8.3 factors.py
# display all the factors of a number chosen by the user

num = int(raw_input("Enter a positive integer: "))
for divisor in range(1, num+1):
    if num % divisor == 0:
        print "{} is a divisor of {}".format(divisor, num)
