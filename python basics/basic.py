#Python Program to Add Two Numbers

# 1) Given two numbers num1 and num2. The task is to write a Python program to find the addition of these two numbers.Given two numbers num1 and num2. The task is to write a Python program to find the addition of these two numbers. 
'''Examples:

Input: num1 = 5, num2 = 3
Output: 8
Input: num1 = 13, num2 = 6
Output: 19'''


#output

# num1=5
# num2=3
# sum=num1+num2
# print("sum is:",sum)


# num1=13
# num2=6
# sum=num1+num2
# print("sum is:",sum)


# num1=15
# num2=12
# sum=num1+num2
# print("sum is:",sum)


# 2)  Adding two numbers with user input


# num1=input("Enter first number")
# num2=input("Enter second number")
# sum=float(num1) + float(num2)
# print("The sum of {0} and {1} is {2}".format(num1,num2,sum))




# 3)   Defining add function and returning the result
# to define  a function that take two integers 
# and return the sum of those integers


# def add(a,b):
#     return a+b
# num1=10
# num2=21
# sum=add(num1,num2)
# print(sum)


# 4) Add two numbers in Python using operator.add() method

# num1=20
# num2=20
# import operator
# sum=operator.add(num1,num2)
# print(" sum of {0} and {1} is {2}" .format(num1,num2,sum) )


# 5) Adding two number using lambda function

# numbers = lambda x , y :  x + y
# num1=20
# num2=6
# sum=numbers(num1,num2)
# print("sum of {0} and {1} is {2}".format(num1,num2,sum))

# 6) Find Maximum of two numbers in Python

# def maximum(a,b):
#     if a>b:
#         return a
#     else: 
#         return b
    
# a=20
# b=30
# print(maximum(a,b))


# 7) Find Maximum of two numbers Using max() function

# a= 2
# b=1

# maximum=max(a,b)
# print(maximum)


# 8) Maximum of two numbers Using Ternary Operator

# a=24
# b=20

# print( a if a>=b else b)

# 9) Maximum of two numbers Using lambda function 


# x=10
# y=9
# maximum=lambda x,y: x if x>y else y
# print(maximum(x,y))


# 10) Maximum of two numbers Using list comprehension



# a=10
# b=9
# maximum=[a if a>b else b]
# print("maximum is:",maximum)


# 11) Maximum of two numbers Using sort() method



# a=10
# b=20
# c=[a,b]
# c.sort()
# print(c[-1])



# 12) To find factorial of a number



# def factorial(n):
     
#     # single line to find factorial
#     return 1 if (n==1 or n==0) else n * factorial(n - 1)
 
# # Driver Code
# num = 5
# print("Factorial of",num,"is",factorial(num))

# next method

# f=1
# num=int(input('Enter your number'))
# if num==0 and num==1:
#     print("factorial is 1")
# for i in range(2,num+1):
#     f=f*i
# print(f)



# 13) Find Compound Interest with Python



#A = P(1 + R/100) t 
#Compound Interest = A – P 
#Where, 
#A is amount 
#P is the principal amount 
#R is the rate and 
#T is the time span


# P=int(input("Enter your principle amount "))
# R=float(input("Enter your Rate "))
# T=int(input("Enter your Time "))
# Amount=(P*(( 1+R / 100)*T))
# Compount_interest=Amount-P
# print("Compount interest is",Compount_interest)


# 14) Given a list, write a Python program to swap first and last element of the list.

# list=[12,35,9,56,24]
# size=len(list)
# print(size)
# Temp=list[0]
# list[0]=list[-1]
# list[-1]=Temp
# print(list)

# another approch
# here the list are assigned for getting swapped(list using the tuple unpaking (means assigning to variables)method)

# list=[12,35,9,56,24]
# list[0],list[-1]=list[-1],list[0]
# print(list)


# 15) Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 

# list=[23,65,19,90]

# list[0],list[-2]=list[-2],list[0]
# print(list)

# 16) How To Find the Length of a List in Python

# list=[10,20,30,40]
# print(len(list))

# 16) Check if element exists in list in Python

# list=[1,6,3,5,3,4]
# if 4 in list:
#    print(True)
# else:
#    pass


# 17) Clear a List using Python List clear()

# list=[1,2,3,4,5]
# list.clear()
# print(list)

# another method
# delete last element in the list


# list=[1,2,3,4,5]
# list.pop()
# print(list)

# another method
# slicing

# list=[1,2,3,4,5]
# print(list[:0])


# 18) Reversing a List in Python

# list=[1,2,3,4,5]
# print(list[::-1])

# another method

# list=[1,2,3,4,5]
# list.reverse()
# print(list)


# 19) Remove an Item from a List


# list=[1,2,3,4,5]
# list.pop(1)
# print(list)


# another method

# list=['amal','martin','joseph','christeena','amurtha']
# list.remove('amal')
# print(list)


# another method

# list=['amal','martin','joseph','christeena','amurtha']
# del list[1:3]
# print(list)

# 20) Python List extend() Method

# list=[1,2,3,4,5]
# list2=[6,7,8,9,10]
# list.extend(list2)
# print(list)

# another appproch of extending a tupple to a list

# list=[1,2,3,4,5]
# tuple=(6,7,8,9,10)
# list.extend(tuple)
# print(list)
  
# extend method with set

# list=[1,2,3,4,5]
# set={6,7,8,9,10}
# list.extend(set)
# print(list)


# 21) from the given list with duplicate values  print list without duplicate values  with out a in built method


# list=[1,2,1,3,4,5]
# list2=[]
# for item in list:
#     if item not in list2:
#         list2.append(item)
# print(list2)


# my_list=[1,2,1,3,4,5]
# my_set=set(my_list)
# new=list(my_set)

# print(new)

# 22) program to find smallest number in the list

# list=[1,2,3,4,5,6]
# print(list[0])

