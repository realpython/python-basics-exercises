# 8.5 review exercises


# Ask the user to enter an integer.
# Repeat the process if the user hasn't entered an integer.
repeat = True
while repeat:
    try:
        myInput = raw_input("Type an integer: ")
        print int(myInput)
        repeat = False
    except ValueError:
        print "try again"

