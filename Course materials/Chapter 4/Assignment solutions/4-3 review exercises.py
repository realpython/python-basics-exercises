# 4.3 review exercises


# print the integer 2 through 10 using a "for" loop
for i in range(2,11):
    print i


# print the integer 2 through 10 using a "while" loop
i = 2
while (i < 11):
    print i
    i = i + 1


def doubles(num):
    ''' Return the result of multiplying an input number by 2 '''
    return num * 2

# Call doubles to double the number 2 three times
myNum = 2
for i in range(0,3):
    myNum = doubles(myNum)
    print myNum

