# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 13:38:25 2020

@author: 66IN
"""


#python examples
'''
#1) add 2 number

x =10
y =20

z=x+y
print(z)


#2) number except number divisible by 3

for i in range(1,10):
    if i%3==0:
        continue
    
    print(i)
    
print("bye")    


#3) patterns 
    
for i in range(5):

    for i in range(5):
        print('# ',end="")
        
    print()    
 
    
for i in range(5):

    for i in range(i):
        print('# ',end="")
        
    print()    
    
  
for i in range(5,0,-1):

    for j in range(i):
        print(j,end="")
        
    print()    


#4) for-else

nums =[12,16,18,21,26]

for num in nums:
    if num%5 == 0:
        print(num)
        
else:
    print("not found")    
    


#5) prime 
num = int(input("enter the number:"))

for i in range(2,num):
    if num % i == 0:
        print("not prime")
        break
else:
    print("prime")    


#6) array from an array

from array import *

vals = array('i',[5,3,-8,9])
 
newArr = array(vals.typecode, (a for a in vals))

for i in newArr:
    print(i)

#7) print array in from user input and search the element's location

from array import *

arr = array('i',[])

n = int(input('enter the length:'))

for i in range(n):
    x = int(input("enter value:"))
    arr.append(x)
    
print(arr)    

val =int(input("enter the value to be searched"))

k=0

for e in arr:
    if e==val:
        print("the position is",k)
        break
    k+=1
    
#can also find index by function 

print("by function ",arr.index(val))    
    
#8) starting with numpy

from numpy import *

arr = array([2,5,6,7.0]) #if any 1 value is float whole array will be float

print(arr.dtype)

print(arr)
   
   
#9) display current-time and date:

import datetime
now = datetime.datetime.now()

print("current date and time")
print(now.strftime("%Y-%m-%d %H:%M:%S"))   



#10) enter user values and convert into list and tuples

values = (input("enter the values"))

list = values.split(",")
tuple = tuple(list)

print("list ",list)
print("tuple ",tuple)


#11) explaining elevator using if statement

user_floor = 6

current_floor = int(input("enter the value here"))

difference = user_floor - current_floor

if difference < 0:
    print("move down")

if difference > 0:
    print("move up")    

#12) if...elif...else statement

number = 3.4

if number > 0:
    print("positive")

elif num == 0:
    print("zero")

else:
    print("negative")    
    
    
#13) odd number in range (1,20)

 odd_numbers = " "

for n in range(1,20):
    if n % 2 != 0:
        odd_numbers=odd_numbers+str(n)+' '
        print(odd_numbers)


#14) for sum of number from 1-1000

number = 0

for i in range(0,1000):
    number = number + i
    
print(number)



#15) to find 10th odd in a given sequence of number

first_num = int(input("Enter the starting number:"))

last_num = int(input("Enter the ending number:"))



nth_odd_num = 0 

count_10th_odd_num = 0

for number in range(first_num,last_num+1):
    if number % 2 != 0:
        nth_odd_num = nth_odd_num + 1
        
        if nth_odd_num == 10:
            count_10th_odd_num=number
            break               #it will break from the for loop
            
print("The 10th odd number is :",count_10th_odd_num)


#16) printing number  multiple times:

for i in range(1,11):
    print(" ")
    
    for j in range(0,i):
        print(i,end=" ")



name = "my name is khan "
print(name.split())



name =" Aditya "
print(name.strip())


name = "aditya1"
print(name.isalpha())


#16) Reversing a string

name = input("enter the name:")

length = len(name)

while length > 0:
    print(name[length -1])
    length = length-1


#17) take user input string and split it and print each word capitalized

name = input("enter the string:")

print(name.split())

for word in name:
    print(word.title(),end="")




#18) occurence of a letter in a word

name = input("enter the word:")

char = input("enter the character to be searched:")

count = 0

length = len(name)

for i in range(0,length):
    if name[i]== char:
        count = count + 1

print(count)        


#19) fibonacci sequence

def fib (n) :
     if n < 0: 
        print("Incorrect input") 
     elif n == 1: 
        return 0
     elif n == 2: 
        return 1    
     
     else: 
        return fib (n - 1) + fib(n -  2)

     
value = fib(5)
print(value)



#20)calculate interest 

def calculate_interest(balance,interest,days):
    interest_amount = balance * (interest/100)*(days/365)
    return interest_amount

print(calculate_interest(1000, 4, 100))



#21) sum of number divisible by 5 in a given range of number
def sum_num(n,m):
    sum = 0
    for n in range(n,m+1):
        if n % 5 ==0:
            sum = sum + n
    return sum
print(sum_num(0,10))    


#22) to have multiple variable , and number of parameters

def avg_grade(*grades):  #with the help of * you can pass multiple arguments
    i =0
    sum = 0.0
    for grade in grades:
        sum = sum + grade
        i = i+1
    avg = sum / i
    return avg

avg = avg_grade(2.5,3.0)
print(avg)    
    
 
#23) sum of all odd number in range

def num_range(n,m):
    sum = 0
    for i in range(n,m+1):
        if i % 2 != 0:
            sum = sum + i
        
    return sum
value = num_range(1,10)
print(value) 
    

#24) example of list

grades = []   #defining empty list grade

while True:
    grade = input("enter the grade:")
    
    if grade =='e':  # e for exit
        break
    
    else :
        grade = float(grade)  #we can directly add float to input fun.
        
        grades.append(grade)  # to add value to the end of the list
            
print(grades) 
    
sum = 0 

for grade in grades:
    sum = sum + grade

print(sum)

avg = sum / len(grades)

print(avg)




#25) number of vowels in a sentence

count = 0

sentence = input("enter the sentence:")
vowels = ['a','e','i','o','u']


for letter in list(sentence):
    if letter in vowels:
        count = count +1 


print(count)




name = input("enter name")

print('Hello {0}'.format(name))



# example of dictionary
grades = {
            "Maths":3.2,
            "English":2.0,
            "Physics":3.7}

print(type(grades))




#26) Calculating total number of vowels occurence in the word / sentence

sentence = input("Enter your sentence:")

vowels = ['a','e','i','o','u']

vowel_count=[]


for i in list(sentence):
    if i in vowels:
        if vowel_count.get(i)==None:  #check already value exist or not
            vowel_count[i]=1
            
        else:
            vowel_count[i]=vowel_count[i]+1


print("result:",vowel_count)




#27) enter a sentence and add the sentence as per vowel in a dictionary

sentence = input("enter the sentence:")
words = []
words = sentence.split()

vowels = ['a','e','i','o','u']

vowels_list ={}

for word in words:
    for letter in words:
        if letter in vowels:
            if vowels_list.get(letter)==None:
                vowels_list[letter]=[word]
                
            else:
                vowels_list.get(letter).append(word)
                

print("result",vowels_list)



#28) example of tuple for the number of student for admission

ages = (4,3,2,6,5,3,7,8,4,2,5)

def primary_school(age):
    if 5>=age>=11:
        return True
    else:
        return False
    
primary_school_age = filter(primary_school,ages)

for age in primary_school_age:
    print(age)    



#29) fibonacci sequence

def fib(n):
    
    a = 0
    b = 1
    
    if n == 1:
        print(a)
    

    else:
        print(a)
        print(b)

    
        for i in range(2,n):
            
            c = a + b

            a = b
            
            b = c
            
            print(c)
            
n = int(input("Enter the number"))

fib(n)


#30) Factorial without recursion


def fact(n):
    
    f=1
   


    for i in range(1,n+1):
        f=f*i
        
    return f


result=fact(5)
print(result)



#31) factorial with recursion

def fact(n):
    
    if(n==0):
        return 1
    
    return n*fact(n-1)




result=fact(5)
print(result)




#32)filter , map ,reduce function

from functools import reduce

nums = [3,2,4,6,7,8,5,9]

evens = list(filter(lambda n:n%2==0,nums))

print(evens)

double = list(map(lambda n: n*2,evens))

print(double)

sum = reduce(lambda a,b:a+b,double)

print(sum)




#33)__init__ method:


class computer:
    
    
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        
    

    def config(self):
        print("conifg is ",self.cpu,self.ram)
        
        

comp1 = computer('i5',8)
comp2 = computer('i7',8) 

comp1.config()
comp2.config()
  

#34) example of class , self , __init__

class employee:
    no_of_leaves = 8
    pass

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
                

    def printdetails(self):
        return f"name is {self.name} , salary is {self.salary} , and his role is {self.role}"


harry = employee("harry", 454,"dev")
rohan = employee()


rohan.name="rohan"
rohan.salary="4454"
rohan.role="dev"


harry.name="harry"
harry.salary="546"
harry.role="se"

print(harry.salary)
print(rohan.printdetails())

#35) init method practise

class dog():
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        
    def sit(self):
        print(self.name.title()+" is sitting")
        
    
    def roll(self):
        print(self.name.title()+" rolled over")
        
        

my_dog=dog("willie",6)

print("my dog name is "+my_dog.name.title()+".")
print("my dog is "+str(my_dog.age)+" years old.")

my_dog.sit()
my_dog.roll()        
  

#36) example 
  
  
class restaurant():
    
    def __init__(self,res_name,cusine_type):
        self.name=res_name
        self.type=cusine_type
        
    
    def describe_res(self):
        print(self.name.title()+" is the best restraunt in the city and known for its "+self.type+".")
        
    

    def open_res(self):
        print(self.name+" is open from 11-11")
        



my_res = restaurant("foodie","indo-italian")

print("The name of restraunt is "+my_res.name)
print("And the cusine type of restraunt is "+my_res.type)

my_res.describe_res()
my_res.open_res()


#37) types of method instance, class,static


class student:

    school='ADedu'    
    
    def __init__(self,m1,m2,m3):
        
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
        
        
    def avg(self):
        return (self.m1+self.m2+self.m3)/3        
   




    @classmethod 
    
    
    def info(cls):
        return cls.school
   
    def get_m1(self):                    #accessor
        return(self.m1)

    def set_m1(self,value):              #mutators
        self.m1=value        
        

    @staticmethod
    
    def into():
        print("This is a tech school.")


s1 = student(34,54,23)
s2 = student(40,44,32)        

print(s1.avg())

print(student.info())

student.into() 



#38) inner class

class student:
    
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop() #inner class obj defined
        
    def show(self):
        print(self.name,self.rollno) 
        self.lap.show()        #inner class obj called



    class laptop:
        
        def __init__(self):
            self.brand='lenovo'
            self.processor='i5'
            self.price=50


        def show(self):
            print(self.brand,self.processor,self.price)
            

s1 = student('adi', 16)

s2 = student('ms',7)

s1.show()
s2.show()


#------------------------//---------------------------# 

def factors(n):
    flist=[]

    for i in range(1,n+1):
        if n%i==0:
            flist.append(i)
    
    return(flist)        


clear=factors(10)

print("the number is:",clear)

#if 2  variable product is more than 1000 than sum else print product


a1 = int(input("enter the variable a:"))
a2 = int(input("enter the variable b:"))


sum = a1 * a2

if sum >= 1000:
    sum = a1 + a2
    print(sum)
    
    
else:
    print("result is ",sum)
    
    

    
#  add next and previous number from list of number
    
list1 = list(range(10))

print("list:",list1)

for n in (list1):
    
    if n+1==10:
        break
    
    else:   
    
        print("n",n)
    
        print("n+1:",n+1)
        
        sum = list1[n]+list1[n+1]
        print("sum:",sum)
    
print("over") 

# enter string and display those characters which are at even indexs
def inputstring_(str):
    for i in range(0,len(str)-1,2):
        print("index [",i,"]",str[i])
     
        

inputstring=input("enter the string:")

print("original string",inputstring)

print("result")
inputstring_(inputstring)



#given a list of number if first and last number is same return true


def input__(number):
    print("number list:",number)
    firstnumber=number[0]
    lastnumber=number[-1]
    
    if (firstnumber==lastnumber):
        return True
    else:
        return False



inp = input("enter number here:")

number = inp.split()

print(number)

print("resutl:",input__(number))



#given list of number ,print number divisible by 5


def div__(number):
    
    for i in number:
        if i%5==0:
            print("number:",i)
            
    
            



number = [10,2,3,5,20]  

div__(number)




#reverse number


def rev(number):
    print("original number:",number)
    original_num=number
    reverse=0
    
    while(number>0):
        remainder = number%10
        reverse=(reverse*10)+remainder
        number = number//10
        
    if (original_num==reverse):
        return True
    
    else:
        return False
    

print("the reverse  number is ",rev(127))    

            


#from 2 list enter number in 3rd : even from 1st and odd from 2nd


def gt__(l1,l2):
    print("first list",l1)
    print("second list",l2)
    l3 = []
    for num in l1:
        if num%2!=0:
            l3.append(num)
            
            
            
         
    for num in l2:
        if num % 2  ==0:
            l3.append(num)
    return  l3   
    




l1 = [1,43,562,53,75]
l2 = [123,343,112,642,47]


print("result",gt__(l1,l2))


#cipher

input_ =input("enter 1st value:")
input_2 =input("enter 2nd value:")

list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
       'v','w','x','y','z']

l2=[]
for i in list1:
    l2=list1.index(input_)+list1.index(input_2)
    
    
print(l2)
print(list1[l2])

'''

import random as rm
'''
deck =list(range(1,53))
print(deck)

rm.shuffle(deck)

print(deck)

value = rm.randint(1,10)
print(value)

result = rm.choice(deck)

print(result)

rsult = rm.choices(deck,k=5)
print(rsult)




# guessing game using random module

while True:
    flag=True
    while flag:
        num = input("Enter the valid number : ")
        
        if num.isdigit():
            print("lets play")
            num = int(num)
            flag =  False
        
        else:
            print("Invalid Input! Try Again")
            
            
            
    secret = rm.randint(1,num)

    guess = None

    count = 1
    
    while guess != secret:
        
        guess=input("guess the number from 1: to "+str(num)+": ")
        if guess.isdigit():
            guess = int(guess)
            
        
        if guess == secret:
            print("You got it!")
            
            
        else:
            print("please try again")
            count +=1
            
           
        

    print("it took you",count,"to guess")
    
  '''
'''
#user input list and adding total 

n=int(input("enter your number of elements :"))


list1=[]

for i in range(0,n):
    ele=int(input())
    list1.append(ele)
    
print(list1)
    

total = 0  
  
for i in list1:
    total += i
    
print(total) 
   


n = int(input("enter the number of input:"))

list1=[]

for i in range(0,n):
    ele=int(input())
    list1.append(ele)
print(list1)

a=max(list1)
print("max number is ",a)



  
import os

print(os.getlogin())
print(os.getpid())
print(os.listdir(path=None))



def fibonacci():
    a,b=0,1

    while True:
        yield a
        a,b=b,a+b
        
        print(a,b)
        

print(fibonacci())        
        
  '''

import random as rm


value = rm.random()
print(value)

print(rm.uniform(0,1))

print(rm.randint(1,10))

print()     











      


     
        

