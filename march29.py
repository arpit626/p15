#que 23 : print all no which are either 


# n = int(input("please enter a no"))

# for i in range(1,n+1):
#     if i % 3 == 0 or i % 5 == 0:
#         print(i)


#que 24: print all the factors of a number

# n = int(input("please enter a number"))

# for i in range(1,n+1):
#     if n%i==0:
#         print(i)


#que 25: print sum or all factors 50 -1 +2+5+10+25=43

# n=int(input("enter a no"))
# sum = 0
# for i in range(1,n):
#     if n%i==0:
#         sum = sum+i

# print(sum)


#que26: accept a no and check if it a perfect no or not
   #    a number whose sum of a factotrs 

n = int(input("enter a number"))
for i in range (1,n):
    if n%i ==0:
        sum = sum +i

if sum == n:
    print("perfect no")
else:
    print("not a perfect no")    

     
