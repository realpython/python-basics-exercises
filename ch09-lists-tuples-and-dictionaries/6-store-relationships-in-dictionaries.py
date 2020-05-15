# 9.6 - Store Relationships in Dictionaries
# Solutions to review exercises


# Exercise 1
# Create an empty dictionary
captains = {}


# Exercise 2
# Add some key-value pairs to the dictionary
captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"


# Exercise 3
# Check if "Enterprise" and "Discovery" exist; if not, add them
if "Enterprise" not in captains:
    captains["Enterprise"] = "unknown"
if "Discovery" not in captains:
    captains["Discovery"] = "unknown"

# Bonus points: you could instead loop over a list of names to check
# for ship in ["Enterprise", "Discovery"]:
#    if not ship in captains:
#        captains[ship] = "unknown"


# Exercise 4
# Display the contents of the dictionary, one pair at a time
for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}.")


# Exercise 5
# Remove "Discovery"
del captains["Discovery"]


# Exercise 6 (Bonus)
# Create dictionary by passing a list to dict()
captains = dict(
    [
        ("Enterprise", "Picard"),
        ("Voyager", "Janeway"),
        ("Defiant", "Sisko"),
    ]
)
