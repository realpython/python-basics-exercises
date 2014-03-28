# 8.3 review exercises


# Display whether the length of user input is <, > or = 5 characters
myInput = raw_input("Type something: ")

if len(myInput) < 5:
    print "Your input is less than 5 characters long."
elif len(myInput) > 5:
    print "Your input is greater than 5 characters long."
else:
    print "Your input is 5 characters long."

