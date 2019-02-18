# 6.4 - Run in Circles
# Solutions to review exercises


# Exercise 1
# print the integer 2 through 10 using a "for" loop
for i in range(2, 11):
    print(i)


# Exercise 2
# print the integer 2 through 10 using a "while" loop
i = 2
while i < 11:
    print(i)
    i = i + 1


# Exercise 3
def doubles(num):
    """Return the result of multiplying an input number by 2."""
    return num * 2


# Call doubles() to double the number 2 three times
my_num = 2
for i in range(0, 3):
    my_num = doubles(my_num)
    print(my_num)
