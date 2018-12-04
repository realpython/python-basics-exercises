# 6.1 - Write Your Own Functions
# Solutions to review exercises


# Exercise 1
def cube(num):
    """Return the cube of the input number."""
    cube_num = num * num * num
    return cube_num


print("0 cubed is", cube(0))
print("2 cubed is", cube(2))


# Exercise 2
def multiply(num1, num2):
    """Return the result of multiplying two input numbers."""
    return num1 * num2


mult_result = multiply(2, 5)
print("2 times 5 is", mult_result)
