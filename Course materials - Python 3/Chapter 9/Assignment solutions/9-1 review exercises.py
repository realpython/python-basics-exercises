# 9.1 review exercises


desserts = ["ice cream", "cookies"]

# Sort the desserts list alphabetically
desserts.sort()

# Display the sorted list
print(desserts)

# Display the index value of "ice cream"
print(desserts.index("ice cream"))

# Copy the contents of the "desserts" list into a new "food" list
food = desserts[:]

# Add some food to the list
food.append("broccoli")
food.append("turnips")

# Display the contents of both lists
print(desserts)
print(food)

# Take "cookies" out of the "food" list
food.remove("cookies")

# Display the first two items in the "food" list
print(food[0:2])

# Create a "breakfast" list full of cookies and display it
my_breakfast = "cookies, cookies, cookies"
breakfast = my_breakfast.split(", ")
print(breakfast)
