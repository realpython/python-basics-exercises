# 4.8 - Find a String in a String
# Solutions to review exercies


# Exercise 1
# Cannot find the string "a" in the string "AAA":
print("AAA".find("a"))


# Exercise 2
# Replace every occurrence of the character `"s"`
# with the character `"x"`
phrase = "Somebody said something to Samantha."
phrase = phrase.replace("s", "x")
print(phrase)
# NOTE: This leaves the capital "S" unchanged, so the
# output will be "Somebody xaid xomething to Samantha."


# Exercise 3
# Try to find an upper-case "X" in user input:
my_input = input("Type something: ")
print(my_input.find("X"))
