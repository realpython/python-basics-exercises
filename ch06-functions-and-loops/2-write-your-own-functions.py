# 6.2 - Write Your Own Functions
# Solutions to review exercises


# Exercise 1
#custom function named cube with parameter num and return cube_num
def cube(num):
    """Return the cube of the input number."""
    cube_num = num**3  # Could also use pow(num, 3)
    return cube_num

#print statements
print(f"0 cubed is {cube(0)}")
print(f"2 cubed is {cube(2)}")


# Exercise 2
#custom function named greet with parameter name
def greet(name):
    """Display a greeting."""
    print(f"Hello {name}!")

#calling function greet by passing in a string
greet("Guido")
