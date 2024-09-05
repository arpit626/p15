
# tuples -  tuple is the collection of heterogeneous type of sata which is store data (creat and read the data but canot the add the value)
t = ()
t = tuple()
t = 1,2,3,4,5,6,8
t = ("hello",[],(1,2,3))
print(t)


t = (12,34,56,90,98)
print (t[1])
print (t[-1])
print (t[1:5:2])  
# cannot delete and update element in tuple


t = (12,34,56,90,98)
print(dir(t))
print(t.count(10))
print(t.index(10)) 


for i in t:
    print(i)

i = 0
while i < len(t):
    print(t[i])
    i += 1    





# sets
s = set()
s = {1,2,3,4,5,6}
print(s)

# operatins of sets
"add","clear","copy","pop","remove","discard"

s.add(6)
s.clear()
x = s.pop()
print(x)

s.discard(123)
s.remove(123)
s.update({21,23,87})
print(s)


for i in s:
    print(i)



# 24 april class
# Sets

# sets me koi element repeat nhi hota ye ek unique rhta he
#ex -> a = {1,2,3,4}

# disadvantage
# duplicate not allow
# method and function difference (method use krne se phle .dot lgta he but function me nhi lgta)
# deep copy and shallow copy pdna he
# list tupple set dict -> follo the deep copy 
# array numpy array -> shallo copy 

# intersection or union
a = {1,2,3,4,5}
b = {3,4,5,6,7}
print(a.difference(b)) # or print(a-b)


# diff update method
a = {1,2,3,4,5}
b = {3,4,5,6,7}
a.difference_update(b)
print(a)


# discard method
x = {"apple","banana","cherry"}
x.discard("apple")
print(x)


#intersection mthod
a = {1,2,3,4,5}
b = {3,4,5,6,7}
print(b.intersection(a))

# union method
a = {1,2,3,4,5}
b = {3,4,5,6,7}
print(b.union(a))


#issubset method
a = {1,2,3,4,5,6}
b = {4,5,6,7,8}





# 26 april class
# set comprehension
s = {1,2,3,4,5,6,7,8,9}
x = {i for i in s if i != 5}
print(s)
print(x) 


# dictionary (key and value)

# creation of dict 
d = {}
d = dict{}

d = {"arpit": "raghuwanshi","age":13}
print(d)


#operation
#read
print(d["arpit"])

#update
d["arpit"] = "vikku"

#delete
del  d["arpit"]
del d["arpit"], d["age"]
print(d)


#clear
d = {"arpit": "raghuwanshi","age":13}
d.clear()

#copy
x = d.copy()
x["age"] = 90

print(d.get("address"))

print(d.items())
print(d.values())
print(d.keys())

x = d.pop("arpit")
print(x)

x = d.popitem()
print(x)


d.update({"age": 134, "address":"bhopal"})
print(d)


#dict compresion
#traversing
for i in d.item():
    print(i)

    