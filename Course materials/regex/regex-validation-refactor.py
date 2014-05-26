import re

validation = re.compile(r'[A-Za-z0-9.]+@[A-Za-z0-9.]+.com$')

email = raw_input("Please enter your email address: ")

while not validation.search(email):
    print "Please enter your email address correctly!"
    email = raw_input ("Please enter your email address: ")

print "\nYour email address is {}!".format(email)
