# 9.6 - Store Relationships in Dictionaries
# Solutions to review exercises


# Exercise 1
# Create an empty dictionary
birthdays = {}


# Exercise 2
# Add some key-value pairs to the dictionary
birthdays["Luke Skywalker"] = "5/25/19"
birthdays["Obi-Wan Kenobi"] = "3/11/57"
birthdays["Darth Vader"] = "4/1/41"


# Exercise 3
# Check if "Yoda" and "Darth Vader exist; if not, add them
if "Yoda" not in birthdays:
    birthdays["Yoda"] = "unknown"
if "Darth Vader" not in birthdays:
    birthdays["Darth Vader"] = "unknown"

# Bonus points: you could instead loop over a list of names to check
# for name in ["Yoda", "Darth Vader"]:
#    if not name in birthdays:
#        birthdays[name] = "unknown"


# Exercise 4
# Display the contents of the dictionary, one pair at a time
for name in birthdays:
    print(name, birthdays[name])


# Exercise 5
# Remove "Darth Vader"
del (birthdays["Darth Vader"])
print(birthdays)


# Exercise 6 (Bonus)
# Create dictionary by passing a list to dict()
birthdays = dict(
    [
        ("Luke Skywalker", "5/25/19"),
        ("Obi-Wan Kenobi", "3/11/57"),
        ("Darth Vader", "4/1/41"),
    ]
)
