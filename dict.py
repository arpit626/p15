#que 48:Pallindromic List- Write a program to check if elements of an List are same or not it read from front or bacExample:arr= [2,3,15,15,3,2]

a = [1,2,3,3,2,1]

j = len(a)-1
for i in range(len(a)//2):
    if a[i] == a[j]:
        j -= 1
        continue
    else:
        print("list is not pallindrome")
        break
else:
   print("list is pallindrome")        
                                


#                 .........Dictionary........   

#que 49:Write a Python program to iterate over dictionaries using for loops
a = {1:67,9:89,5:68}

for i in a.value():
    print(i)


#ex:
a = {1:23,2:45,3:56}
b = {4:67,5:58,6:98}

b.update(a)
print(a)

#//
#kisi dict me nayi key value update function ke bina kese key value bna skte hn
a = {1:23,2:56,7:90}

a [8] = 89
b [3] = 45

print[a]


#que50" Write a Python script to merge two Python dictionaries.
a = {1:29,2:36,3:90}
b = {20:67,10:89,40:90}

for i in b:
    a[i] = b[i]

print(a)    



#// 
#add a new key and value as 5:89
a[5] = 89

#change the value 1 

# add all values
sum = 0
for i in a.value():
    sum = sum + i
print(sum)    


# que 52: convert a list to dict 

a = [10,20,30,40,50]

d = {}

for i in range(len(a)):
    d[i] = a[i]

print(d)   


#Que : 53count the frequency of each elements

a = [1,1,4,4,6,1,2,2,2,2]

d = {}

for i in a:
    if i in d.keys():
       d[i] = d[i] + 1
    else:
        d[i] = 1

print(f"2 occured {d[2]}")           






#que 54: Write a Python program to combine two dictionary by adding values for common keys.

a = {1:34,2:56,3:30}
b = {3:78,5:89,6:10}

for i in b.keys():
    if i in a.keys():
        a[i] = a[i] + b[i]
    else:
        a[i] = b[i]

print(a)            

