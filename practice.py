# for i in range (1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()
 
# for i in range (1,9):
#     z=1
#     for j in range(i):
#         print(f"{j}",end=" ")
#         z = z+1
#     print()     


# for i in range (1,8):
#     z = 1
#     for j in range(i):
#         print(f"{j}" , end = " ")
#         z =z+1 
#     print()   ]

# for i in range(1,5):
#     a = 1
#     for j in range(i):
#         print(f"{j}",end = " ") 
#         a=a+1
#     print()    


# for i in range(1,20):
#     z=65
#     for j in range(i):
#         print(f"{chr(j)}",end=" ")
#         z=z+1
#     print()


# for i in range(1,20): 
#     z=65
#     for j in range(i):
#         print(f"{chr(j)}",end=" ")
#         z=z+1
#     print()    

# for i in range (1,6):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")  
#     print()  


# for i in range (1,9):
#     for j in range(8-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")  
#     print()  

# for i in range (1,9):
#     for j in range(8-i):
#         print("" , end= " ")
#     for k in range(9-i):
#         print("*" , end = " ")
#     print() 




# for i in range(1,9):
#     for j in range(8-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end=" ")
#     print()    

# for i in range(1,9):
#     for j in range(i-1):
#         print("",end=" ")
#     for k in range(9-i):
#         print("*",end=" ")    
#     print()    




# for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end = "")
#     for k in range(i):
#         print("*",end=" ")
#     print() 


# for i in range(1,6):
#     for j in range(i-1):
#         print("", end=" ")
#     for k in range(6-i):
#         print("*", end=" ")
#     print()        




#string que

# a= "this is my phone"
# b = ""

# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]

# if a == b:
#     print("it is a pallindrome")

# else:
#     print("not a pallindrome")




# def dets(name,age,batchcode="p15"):
#      print(f"Name->{name}")
#      print(f"Age->{age}")
#      print(f"batchcode->{batchcode}")

# dets("arpit",22)
# dets("verma",21) 


# def a(gender,height,colour):
#     print(f"Gender -> {gender}")
#     print(f"Height -> {height}")
#     print(f"Colour -> {colour}")


# a("Male",6,"white")   
# a("naman",4,"red")  



# for i in range(1,6):
#     for j in range(i-1):
#         print("", end=" ")
#     for k in range(6-i):
#         print("*", end=" ")
#     print()   

# for i in range (1,9):
#     for j in range(i-1):
#         print("", end=" ")
#     for k in range(8 -i):
#         print("*",end=" ")
#     print()             





# l = [1,2,3,20,4,5,6,56,7,8,9,91,12,13,89,14,15,16,49,17,18,19,99]
# l.append(55)
# print(l)



# t = 1,2,3,4,5,6,7,8,9,0
# print (dir(t))



# a = "i love R34 And 5ou 28ve cs0"

# b = ""
# sum = 0
# for i in a:
#     if i.isdigit():
#        sum = sum + int(i)
#     else:
#        b = b + i

# print(b)
# print(sum) 


# a = "hoe ar3  love yo4 miss poona5 j1 "

# b =""
# sum = 0
# for i in a:
#    if i.isdigit():
#       sum = sum + int(i)
#    else:
#       b = b + i
# print(b)
# print(sum)         



# a = "67rpi7 rag4uwansh1"
# b = ""
# sum = 0
# for i in a :
#     if i.isdigit():
#         sum  = sum + int(i)
#     else:
#         b = b + i
# print(b)
# print(sum)      

# age = 22
# print(f"hello my age is {age}")

# a = " bhopal is warm"

# print(a[10:14:1])      

# a = " how are you pranjal singh "
# print(a[12:20:1])





# a = "hello man"
# for i in range(0,len(a)):
#     # print(a[i])   #/

# a = "arpit"
# for i in range(4,-1,-1):
#     print(a[i])


# a = " today is a hot day "

# b = " "
# c = " "
# for i in a:
#     if i.islower():
#        b = b + i
#     elif i.islower():
#        c= c + i

#print(b+c)  



# a = "today is your exam "
# b = ""
# c =""
# for i in a:
#    if i.islower():
#       b = b+i
#    elif i.islower():
#       c = c+i
# print(b+c)      


# a = {1:29,2:36,3:90}
# b = {21:67,10:89,40:90}

# for i in a:
#     b[i] = a[i]

# print(a) 



# a = [10,20,30,40,50]

# d = {}

# for i in range(len(a)):
#     d[i] = a[i]

# print(d) 

# a = [12,34,56,78,99,90]

# d  = {}

# for i in range(len(a)):
#     d[i] = a[i]

# print(d)




# a=int(input("enter your number"))
# r=0
# while a > 0:
#       z=a%10
#       r=r*10+z
#       print(a%10) 
#       a=a//10
# print(r)



# salary=int(input("enter your salary"))

# if salary < 300000:
#     print("No tax")
# elif salary >= 300000 and salary < 500000:
#     print("you have to pay 10 % tax of your salary which is ",salary*10//100)

# elif salary > 500000 and salary < 700000:
    
#     print("you have to pay 15% tax of your total amount  which is ",salary*15//100)
# elif salary>= 700000:
#     print("20 % tax you have pay in your total salary which is",salary*20//100)

# a="how are you brother"
# b=""
# for i in a :
#     if i !=" ":
#         b+=i
# print(b)


# n=int(input("enter your range"))
# for i in range (1,n+1):
#     A=i
#     count=0
#     for i in range(1,A+1):
#       if A %i==0:
#         count+=1
#     if count==2:
#       print(A)



# a=int(input("enter a number"))
# sum=0
# copy=a

# while a>0:
#     z=a%10
#     sum=sum+z**3
#     a=a//10
# if copy==sum:
#         print("armstrong number")
# else:
#         print("not armstrong")  




# Write a Python program to combine two dictionary by adding values for common keys.

# a = {1:34,2:56,3:30}
# b = {3:78,5:89,6:10}

# for i in b.keys():
#     if i in a.keys():
#         a[i] = a[i] + b[i]
#     else:
#         a[i] = b[i]

# print(a)


# a = {1:23,2:45,3:56}
# b = {4:67,5:58,6:98}

# a = b.update
# print(a)


# a = {1:29,2:36,3:90}
# b = {20:67,10:89,40:90}

# for i in b:
#     a[i] = b[i]

# print(a) 


# a = [1,1,4,4,6,1,2,2,2,2]

# d = {}

# for i in a:
#     if i in d.keys():
#        d[i] = d[i] + 1
#     else:
#         d[i] = 1

# print(f"2 occured {d[2]}")   


#que 54: Write a Python program to combine two dictionary by adding values for common keys.

# a = {1:34,2:56,3:30}
# b = {3:78,5:89,6:10}

# for i in b.keys():
#     if i in a.keys():
#         a[i] = a[i] + b[i]
#     else:
#         a[i] = b[i]

# print(a)    







# a = {4:67,5:90,7:85}
# b = {7:89,1:50,3:78}

# for i in a.keys():
#     if i in b.keys():
#         b[i] = b[i]+a[i]

#     else:
#         b[i] = a[i]

# print(b)        




# 10 may 


# -> higher order function - a function which takes a function as a parameters or return a function or both is known as hof

# -> function call is replaced by its return value

# -> call backs - 

# -> map -

# -> filter - 

# -> zip - chinta chpr aap me kya kr skti 



# def findErrorNums(nums):
    
#     seen = set()
#     duplicate = -1
#     missing = -1
    
#     for num in nums:
#         if num in seen:
#             duplicate = num
#         else:
#             seen.add(num)
    
#     total_sum = sum(range(1, len(nums) + 1))
#     array_sum = sum(nums)
    
#     missing = total_sum - array_sum + duplicate
    
#     return [duplicate, missing]

# print(findErrorNums([1, 2, 2, 4]))  
# print(findErrorNums([1, 1]))         


# a = [1,2,3,4]

# d = {}

# for i in a:
#     if i in d.keys():
#         d[i] +=1
#         print("true")
#         break
#     else:
#         d[i] = 1

# else:
#     print("false")

# r = "aa" 
# m = "aab"

# d1 = {}
# d2 = {}

# for i in r :
#     if i in  d1.keys():
#         d1[i] += 1
#     else:
#         d1[i] = 1    

# for i in m :
#     if i in  d2.keys():
#         d2[i] += 1
#     else:
#         d2[i] = 1  

# for i in d2.key():
#     if i in d2.keys():
#         if d1[i] <= d2[i]:
#             continue
#         else:
#             print("false")
#             break
#     else:
#         print("true")



# x = [1,1]


# for i  in range (len(x)-1):
#     if x[i] == x[i+1]:
#         print([x[i],x[i+1]+1])



# a = [1,2,3,4,5,6,7,8,9,2]  


# d = {}
# for i in a:
#     if i in d.keys():
#         d[i]= d[i]+1
#         print("true")
#         break
#     # else
#         d[i] = 1
# else:
#     print("false") 


# a = [1,2,3]
# d={}
# for i in a:
#     if i in d.keys():
#         d[i] = d[i]+1
#         print("true")
#         break
#     else:
#         d[i]=1

# else:
#     # print("false")        


# a = [1,2,3,4,5,6,7,7]

# for i  in range (len(a)-1):
#     if a[i] == a[i+1]:
#         print([a[i],a[i+1]+1])



# from pathlib import Path
# import os
# import shutil

# def createfolder():
#     try:
#        name = input("please tell your folder name")
#        if name == " ":
#            name == "New Folder"
#        path = Path(name)
#        path.mkdir()
#        print(f"folder name {name} created successfully")
#     except Exception as err:
#         print(f"Error: folder {name} already exist")

# check = int(input("what do you want"))
# if check == 1:
#     createfolder()


# class String: 
      
#     def __init__(self, string): 
#         self.string = string 
          
#     def __repr__(self): 
#         return 'Object: {}'.format(self.string) 
  
# if __name__ == '__main__': 
      
 
#     string = String('Hello')  
#     print(string) 


# class String: 
      
#     def __init__(self, string): 
#         self.string = string 
          
#     def __repr__(self): 
#         return 'Object: {}'.format(self.string) 
  
# if __name__ == '__main__': 
      
 
#     string1 = String('Hello')  
#     print(string1) 


# class number:
#     def __init__(self,num):
#         self.num = num

#     def __add__(self, num2):
#         return self.num + num2.num

#     def __eq__(self,Object):
#         print(self.num == Object.num)

# n1 = number(int(input("Enter the number : ")))
# n2 = number(int(input("Enter the number : ")))

# n1 = number(4)
# n2 = number(5)


# Inheritance 

# class Employee:
#     def __init__ (self,name,id):
#         self.name = name
#         self .id = id
#     def showDetails(self):
#         print(F"The name of Employee : {self.id} is {self.name}")

# class Programmer(Employee): #  Employee is a parent class and programmer is child class so the programmer is inherit all properties (like name , id ) of employee class. 
#     def showLanguage(self):
#         print("The Default Language is Pyhton")



# e1 = Employee ("Arpit Raghu" , 18 )
# e1.showDetails()
# e2 = Employee("vikku", 20)
# e2.showDetails()
# e2.showLanguage()








# 24june
# data classees
# from dataclasses import dataclass
# @dataclass
# class Person:
#     __name: str
#     __age: int

#     def __str__(self):
#         return f"{self.__name} is  {self.__age} years old "     
    

# a = Person("Arpit",22)  
# print(a) # arpit is 22 years old 




#2   
# from collections import namedtuple


# Det = namedtuple("Details",["name","age"])
# x = Det("vikku",25)
# print(type(x))
# print(x) 

a = "123"

b = ""

for i in range(len(a)-1,-1,-1):
    b = b + a[i]

if a== b:
    print("true")
else:
    print("false")             


