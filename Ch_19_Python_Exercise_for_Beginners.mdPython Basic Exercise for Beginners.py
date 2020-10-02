Python Basic Exercise for absolute Beginners

# Question 1 . Write a program to input eight numbers from the user . All numbers will be unique 

# Solution 1 : 

# this is the program
number1  = int(input("Enter the value of number 1"))
number2  = int(input("Enter the value of number 2"))
number3  = int(input("Enter the value of number 3"))
number4  = int(input("Enter the value of number 4"))
number5  = int(input("Enter the value of number 5"))
number6  = int(input("Enter the value of number 6"))
number7  = int(input("Enter the value of number 7"))
number8  = int(input("Enter the value of number 8"))


myset = {number1 ,number2 ,number3 ,number4 ,number5 ,number6 ,number7 ,number8}

print(myset)



# Question 2 : Write a program to calculate profit percentage from the sales that you made ?

# Solution 2 : ''' gos : goods sold cost
                 revn : rate at which goods sold
                 porl : profit or loss

'''

gos = float(input("Enter the cost of goods sold : "))
revn = float(input("Enter revenue amount : "))
porl = revenue - gos
profit_Percentage = porl/gos*100
print("Cost of goods :",gos)
print("Revenue generated from sales :",revn)
print("Cost of goods :", profit_Percentage)

# Question 3 : What will be the output of the following python code

myname = 'Mike'
myage = 26
print(myname,",you are",myage,"now but \n",end='')
print("you will be", myage + 1 ,"next year")

# Solution 3 : Output will be

''' 

Mike ,you are 26 now but
you will be 27 next year

'''
# Question 4 :  Write a program to calculate BMI of a human.

# Solution 4 : # Program will be

weight_in_kg = float(input("Enter the weight in Kilpgram"))
height_in_meter = float(input("Enter the height in meteres "))
BMI = weight_in_kg/(height_in_meter*height_in_meter)
print("Your BMT is : ",BMI)

# Question 5 : Write a program to input a welcome message and print it.

# Solution 5 : # Program will be

Printwel = input("Enter the welcome message :")
print()
print("hello",Printwel)
















