# 9.3 review exercises


# Create an empty dictionary
birthdays = {}

# Add some key-value pairs to the dictionary
birthdays["Luke Skywalker"] = "5/25/19"
birthdays["Obi-Wan Kenobi"] = "3/11/57"
birthdays["Darth Vader"] = "4/1/41"

# Check if "Yoda" and "Darth Vader exist; if not, add them
if not "Yoda" in birthdays:
    birthdays["Yoda"] = "unknown"
if not "Darth Vader" in birthdays:
    birthdays["Darth Vader"] = "unknown"

## Bonus points: you could instead loop over a list of names to check
#for name in ["Yoda", "Darth Vader"]:
#    if not name in birthdays:
#        birthdays[name] = "unknown"

# Display the contents of the dictionary, one pair at a time
for name in birthdays:
    print name, birthdays[name]

# Remove "Darth Vader"
del(birthdays["Darth Vader"])
print birthdays


# Bonus: could have created dictionary by passing a list to dict()
birthdays = dict([("Luke Skywalker", "5/25/19"),
                  ("Obi-Wan Kenobi", "3/11/57"),
                  ("Darth Vader", "4/1/41")])

