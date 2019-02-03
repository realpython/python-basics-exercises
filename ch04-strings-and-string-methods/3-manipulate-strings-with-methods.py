# 4.3 - Use String Methods
# Solutions to review exercies


# Exercise 1
string1 = "Animals"
string2 = "Badger"
string3 = "Honey Bee"
string4 = "Honeybadger"

print(string1.lower())
print(string2.lower())
print(string3.lower())
print(string4.lower())


# Exercise 2
print(string1.upper())
print(string2.upper())
print(string3.upper())
print(string4.upper())


# Exercise 3
string1 = "    Filet Mignon"
string2 = "Brisket    "
string3 = "  Cheeseburger   "

print(string1.strip())  # Could also use .lstrip()
print(string1.strip())  # Could also use .rstrip()
print(string3.strip())


# Exercise 4
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = "  bEautiful"

print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))


# Exercise 5
string1 = string1.lower()
# (string2 will pass unmodified)
string3 = string3.lower()
string4 = string4.strip().lower()

print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))
