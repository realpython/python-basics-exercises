# 9.1 review exercises


desserts = ["ice cream", "cookies"]

# Sort the desserts list alphabetically
desserts.sort()

# Display the sorted list
print desserts

# Display the index value of "ice cream"
print desserts.index("ice cream")

# Copy the contents of the "desserts" list into a new "food" list
food = desserts[:]

# Add some food to the list
food.append("broccoli")
food.append("turnips")

# Display the contents of both lists
print desserts
print food

# Take "cookies" out of the "food" list
food.remove("cookies")

# Display the first two items in the "food" list
print food[0:2]

# Create a "breakfast" list full of cookies and display it
my_breakfast = "cookies, cookies, cookies"
breakfast = my_breakfast.split(", ")
print breakfast

"""
Define a function that takes a list of numbers, `[2, 4, 8, 16, 32, 64]`, as the
argument and then outputs only the numbers from the list that fall between 1
and 20 (inclusive)
"""


def print_list(list_of_nums):
    for num in list_of_nums:
        if num >= 2 and num <= 20:
            print num

list_of_numbers = [2, 4, 8, 16, 32, 64]
print_list(list_of_numbers)
