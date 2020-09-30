# 3.3 - Create a Variable
# Solutions to review exercies


# Exercise 3 (exercises 1 and 2 are done in interactive window)
# This solution works for Exercises 1 and 2 by typing the same lines into the
# interactive window.

# Display a string directly
print("hello")


# Display the contents of a string variable
my_string = "hi"
print(my_string)


# Declare variables
sample_string = "Hello"
sample_int = 123

#To concat and display both the above variables, the integer variable needs to be typecasted !!
print(sample_string + str(sample_int))
# Can also be written using F-string
print(f"{sample_string + str(sample_int)}")
