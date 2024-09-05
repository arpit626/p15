Que:1 #if else que. 
#Create a python program to calculate the total tax payble to all the government if the salary is below 3 lakh the person has to pay 
#no tax if the salary is above 3 lakh 10% tax above 5 lakh 15% tax above 7 lakh 20% tax

salary=int(input("enter your salary"))

if salary < 300000:
    print("No tax")
elif salary >= 300000 and salary < 500000:
    print("you have to pay 10 % tax of your salary which is ",salary*10//100)

elif salary > 500000 and salary < 700000:
    
    print("you have to pay 15% tax of your total amount  which is ",salary*15//100)
elif salary>= 700000:
    print("20 % tax you have pay in your total salary which is",salary*20//100)





Que:2 # you are given a number print the reverse of that number you cannot use string function

a=int(input("enter your number"))
r=0
while a > 0:
      z=a%10
      r=r*10+z
      print(a%10) 
      a=a//10
print(r)





Que:3 # a=int(input("enter a number"))
# print([::-1]


# string se space remove karna hai  



a="how are you brother"
b=""
for i in a :
    if i !=" ":
        b+=i
print(b)





Que:4 # #print prime number 1 to 10 
# a=15
# count=0
# for i in range(1,a+1):
#     if a%i==0 :
#         count=count+1
#         print(i)

#akrsh bhaiya 
n=int(input("enter your range"))
for i in range (1,n+1):
    A=i
    count=0
    for i in range(1,A+1):
      if A %i==0:
        count+=1
    if count==2:
      print(A)




Que: 5 # armstrong number
a=int(input("enter a number"))
sum=0
copy=a

while a>0:
    z=a%10
    sum=sum+z**3
    a=a//10
if copy==sum:
        print("armstrong number")
else:
        print("not armstrong")       