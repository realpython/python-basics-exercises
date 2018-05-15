import re

validation = re.compile(r'[A-Za-zs.]')

name = input("Please enter your name: ")

while not validation.search(name):
    print("Please enter your name correctly!")
    name = input("Please enter your name: ")

print("\nYour name is {}!".format(name))
