# while loop ex (program ko hum jab tak continue karte he jb tk 0 na ho jaye)

# a = 123
# print(a%10)
# a = a//10
# print(a%10)
# a=a//10
# print(a%10)

# que:27 seperate each digit of a no and print it on the new line
# n = int(input("enter a no"))

# while n > 0:
#     print(n%10)
#     n=n//10





#que sum 
# n = int(input("enter a no"))
# sum = 0
# while n > 0:
#     sum = sum + n%10
#     n  = n//10

# print(sum)    




# que check if a no is prime is not
# n = int(input("enter a no"))
# count = 0

# for i in range(1,n+1):
#     if n%i ==0:
#         count = count + 1

# if count == 2:
#     print("prime no")
# elif count > 2:
#     print("not prime or composite no")  
# else:
#      print("unity number")       



#que 29;accept a no and print it reverse

n = int(input("please enter a number"))
rev = 0
while n>0:
    z = n%10
    rev = rev *10 + z
    n = n//10

print(rev)    


#que30
n = int(input("please enter a number"))
copy = n
rev = 0
while n>0:
    z = n%10
    rev = rev *10 + z
    n = n//10

if copy == rev:
    print("palindrome no")

else:
    print("not a palindrome") 
    








