# 9.2 - Lists are Mutable Sequences
# Solutions to review exercises


# Exercise 1
# Create a list named food with two elements "rice" and "beans".
food = ["rice", "beans"]


# Exercise 2
# Append the string "broccoli" to the food list using .append()
food.append("broccoli")


# Exercise 3
# Add the strings "bread" and "pizza" to food using .extend()
food.extend(["bread", "pizza"])


# Exercise 4
# Print the first two items in food using slicing notation
print(food[:2])

# NOTE: The following is also acceptable
print(food[0:2])


# Exercise 5
# Print the last item in food using index notation
print(food[-1])


# Exercise 6
# Create a list called breakfast from the string "eggs, fruit, orange juice"
breakfast = "eggs, fruit, orange juice".split(", ")


# Exercise 7
# Verify that breakfast has three items using len()
print(len(breakfast) == 3)


# Exercise 8
# Create a new list called `lengths` using a list
# comprehension that contains the lengths of each
# string in the `breakfast` list.
lengths = [len(item) for item in breakfast]
print(lengths)
