# procedural progtamming paradigm - isme hum output nikalte he bs , isme koi jrurt nhi rehti ki output kis way me he 

# functional programming paradigm - function me  hum code ko ek bar likhte he or jitni baar output chaiye utni baar le skte hn or isme hum hum output kese chiye bese le skte he
# non parametrized function and impure fuction ka use nhi karege kv bht hi jrurt pdne pr hi karege othetrwise nhi

# functions statement
# syntex of function decleration / definition
# def funcname():
#     print("hello")
#     print("world")


# types of function

#impure function(code ki bahar ki cheeje lete hn use impure function kehte hn)
# time = "evening"
# def greet():
#     print(f"good{time}")


# greet()


# pure function (code ke andar se cheeje lete he jise pure function bolte he)
# def greet():
#     time= "evening"
#     print(f"good{time}")

# greet()   


# non parametrized function(value bahar se nhi le skte)
# time = "evening"
# def  greet():
#     print (f"good{time}")

# greet()



# parametrized function(aese function jo bahar ki value ko ander le aaye bo parametrized function hote he)

# def  greet(time): #parameter of the function
#     print (f"good{time}")

# greet ("evening") # argument of the function 
# greet ("morning") # argument of the function

# def sum(a,b):
#     add = a + b
#     print(add)

# n1  = int(input("number 1: "))
# n2  = int(input("number 2: "))
# sum(n1,n2)



# # Lambda function expression (single line function)

# def sum(a,b):
#     print (a+b)

# # variable = lambda parameterized : single line erpression
# sum = lambda a , b : print(a+b) 
# sum (1,2)




# create a function which find the product of two values , 
# and further the values can divide by given users input

# function with return to return the result of the function out of the function scope
# function call is replaced by its return value


# def product (a,b):
#     x = a * b
#     return x

# a = 12
# b = 4
# res = product (a,b)
# c = 2

# print(product(a,b))



# a function can have only one return and that must be the last line of the function
# we can return only single entity from the function


# variable lenght input argument in the function 
# *args must be the last parameter in the function definition  
# we can use only 1 *args in a functon definition 
# def apnaprint(*a):
#     print (a)


# apnaprint("hello world ","hello world 2","hello world 3")  




# #example:
# def dets(name,batch,hobbies):
#     print("name: ",name)
#     print("batch: ",batch)
#     print("hobbis: ", hobbies)

# dets("john","2020")
# dets("john","2020","reading")    
# dets("john","2020","reading","playing cheess")    
# dets("john","2020","reading","playing chess","coding")    



# lambda function exp (are the function whuch return in only singke line)

# function statement
# def sum(a,b):
#     return a + b


# # function exp
# sum = lambda a,b: a+b
# # variable = lambda parametrs : return_value


# print(sum(1,2))



# default params

# key points - default parametr must be last parametrs 
#            - there should be one default parametrs in a function
# def dets(name,age,batchcode="p15"):
#     print(f"Name -> {name}")
#     print(f"Age -> {age}")
#     print(f"Batch Code -> {batchcode}")


# dets("john",12)
# dets("john",12,"MERN")  




# # keywords arguments(isme hum sequence wise parametrs ka use krte he )
# # Given parameteres are -> batchcode, name and age
# def dets(name, age, batchcode="P15"):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"Batch: {batchcode}")
    
# dets(age=20, name="Rahul", batchcode="Python")





# stack(lifo)
# Day 19 notes

# Stack - LIFO (Last In First Out) or FILO (First In Last Out)
# Stack is a linear data structure which follows a particular order in which the operations are performed.
# Example-
# '''''
# # def hello1():
# #     hello2()
# #     print(1)
    
# # def hello2():
# #     hello3()
# #     print(2)
    
# # def hello3():
# #     hello4()
# #     print(3)
    
# # def hello4():
# #     print(4)
    
# # hello1()
# # '''''
# # Recursion - A function calling itself
# # Example-
# def hello(n):
#     if n == 0:
#         return
#     else:
#         hello(n-1)
#         print(n)
# hello(10)
# '''''
# '''''
# def hello(n):
#     if n == 0:
#         return
#     else:
#         print(n)
#         hello(n-1)
        
# hello(10)
# '''''
# # Write a program using function to check if a number is pallidrome or not
# '''''
# def pallindrome(x):
#     copy = x
#     rev = 0
#     while x > 0:
#         rev = rev*10 + x%10
#         x = x//10
        
#     if copy == rev:
#         return True
#     else:
#         return False
    
# a = int(input("Enter a number: "))
# if pallindrome(a):
#     print("Pallindrome")
# else:
#     print("Not Pallindrome")


# Your task is to go through all the question that has been done in the previous days and try to solve them.(by functions)





# 19 april class


# Premitive data types 
# It is a data type that is not an object and has no methods. It is a basic data type provided by a programming language.
# These are mutable data types. It basically creates a copy of a variable and stores it in a different memory location.
'''''
a = 5 
b = a 
a = 10
print(a)
print(b)
'''''
# Reference data types

# List  - denoted by [] & empty list is created by list()
# List is a collection of items that are ordered and changeable. Allows duplicate members. This is a important data type in python. It is a sequence data type that can store a collection of items.
'''''
a = [10]
b = a
a[0] = 200
print(a)
print(b)
'''''
# For accessing the elements in a list, we use indexing to itirarte through the list. Indexing starts from 0.
# Example: print(list[start:end:step]) - in this step is the increment value.
'''''
a = [10, 20, 30, 40, 50]
print(a[0])
print(a[1:4:2])
'''''
# List methods - append(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), copy()
# del - to delete the element from the list, it is same is remove() but remove() is used to remove the element by value and del is used to remove the element by index.
'''''
# In this there is a example of list slicing and deletion
l = [21, 34, 56, 78, 90, 90, 78, 56, 54, 23, 10]
# print(l[-6:-11:-1])
del l[1]
print(l)
'''''

# Tuple - denoted by ()
# Tuple is a collection of items that are ordered and unchangeable. Allows duplicate members. It is a sequence data type that can store a collection of items. It is immutable. It is sequence data type that can store a collection of items.



# Set - denoted by {} & empty set is created by set()
# Set is a collection of items that are unordered and unindexed. No duplicate members. It is a collection of items that are unordered and unindexed. It is mutable. It is a collection of items that are unordered and unindexed. It is a collection of items that are unordered and unindexed.



# Dictionary - denoted by {key:value} & empty dictionary is created by {}
# Dictionary is a collection of items that are unordered, changeable and indexed. No duplicate members. It is a collection of items that are unordered, changeable and indexed. It is mutable. It is a collection of items that are unordered, changeable and indexed. It is a collection of items that are unordered, changeable and indexed.