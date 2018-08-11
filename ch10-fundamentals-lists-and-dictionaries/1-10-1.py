# 1.10.1 - Lists: Multipurpose Containers
# Solutions to review exercises


# Exercise 1
desserts = ["ice cream", "cookies"]


# Exercise 2
# Sort the desserts list alphabetically and display the sorted list
desserts.sort()
print(desserts)


# Exercise 3
# Display the index value of "ice cream"
print(desserts.index("ice cream"))


# Exercise 4
# Copy the contents of the "desserts" list into a new "food" list
food = desserts[:]


# Exercise 5
# Add some food to the list
food.append("broccoli")
food.append("turnips")


# Exercise 6
# Display the contents of both lists
print(desserts)
print(food)


# Exercise 7
# Take "cookies" out of the "food" list
food.remove("cookies")


# Exercise 8
# Display the first two items in the "food" list
print(food[0:2])


# Exercise 9
# Create a "breakfast" list full of cookies and display it
my_breakfast = "cookies, cookies, cookies"
breakfast = my_breakfast.split(", ")
print(breakfast)


# Exercise 10
# Define a function that takes a list of numbers, `[2, 4, 8, 16, 32, 64]`, as
# the argument and then outputs only the numbers from the list that fall
# between 1 and 20 (inclusive)
def print_list(list_of_nums):
    for num in list_of_nums:
        if num >= 2 and num <= 20:
            print(num)


list_of_numbers = [2, 4, 8, 16, 32, 64]
print_list(list_of_numbers)
