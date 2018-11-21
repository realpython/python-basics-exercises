# 4.8 - Find a String in a String
# Solutions to review exercies


# Exercise 1
# Cannot find the string "a" in the string "AAA":
print("AAA".find("a"))


# Exercise 2
# Try to find a number inside a string;
# use str() to convert the number first
version = "version 2.0"
v_num = 2.0
print(version.find(str(v_num)))


# Exercise 3
# Try to find an upper-case "X" in user input:
my_input = input("Type something: ")
print(my_input.find("X"))
