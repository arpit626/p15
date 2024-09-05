
# Day 1 (string)
# string slicing

age = 22
print(f"hello my age is {age}")

a = " bhopal is warm"

print(a[10:14:1])



#  string methods

# a = "hellow"
# print(a.upper())

# string me hum do type me loop chla sakte hai one is with indexing or second is without indexing

#/ string traversing
a = "hello man"
for i in range(0,len(a)):
    print(a[i])   #/

a = "hello man" # reverse printing of hello
for i in range(4,-1,-1):
    print(a[i])







# Day 2 (String)


a = " today is a hot day"

b = ""

for i in a:
    if i.islower():
       b = b+i
    elif i.islower():
       c= c+i


print(b+c)       



# que 33 :    

a = "P@#yn26at^&i5ve"

char = 0
spchar = 0
digit = 0

for i in a :
    if i.isalpha():
       char = char + 1
    elif i.isdigit():
       digit = digit + 1
    elif i != " ":
       spchar = spchar + 1      

print(f"total characters are {char}")
print(f"total special characters are{spchar}") 
print(f"total digits are{digit}")       


#que   a = " RCB will win IPL "
# print BCR lliw niw LIP"

c = ""
for i in range(len(a)):

    if a[i] == " " :
        b = ""
        for i in range(i-1,-1,-1):
             if a[i]  == " ":
                 break         
             b = b+a[i]             
        c = c + " " + b

k = " "
for i in range(len(a)-1,-1,-1):
     if a [i] == " " :
         break
                 
     k = k + a[i] 
c = c + " " + k

print(c)



#uqe homework

a = "123v how ar3 yo5"

print(14)
print(" v how ar yo")   


# que;
a = "i love R34 And 5ou 28ve cs0"

b == ""
sum = 0
for i in a:
    if i.isdigit():
       sum = sum + int(i)
    else:
       b = b + i

print(b)
print(sum)   





# que34
# inbuilt function are check the similarty
# for ex

# a = "hello"
# b = "hello"

# if len(a) != len(b):
#     print("not same ")
# else:
#    for i in range(len(a)):
#        if a[i] == b[i]:
#            continue
#        else:
#            print("your stirng are not same")
#            break
#    else:
#        print("your string are same")


# que 35;
# a = "wow a beautiful summer"

# count = 0

# for i in a:
#     if i in  "aeiouAEIOU":
#          count +=1

# print(count)



# que36: revere a string
a = "brother"

b = ""

for i in range(len(a)-1,-1,-1):
    b = b + a[i]

print(b)



#que 37 check string is palindrome or not

a = "brother"

b = ""

for i in range(len(a)-1,-1,-1):
    b = b + a[i]

if a== b:
    print("pallindrome")
else:
    print("not a palindrome")      