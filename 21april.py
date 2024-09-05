
## traversing the list(means read krna)

#traversing by the for loop
l = [2,4,5,6,7,3,8,9]

for i in l : 
    print(i/2)

# by while loop
i = 0
while i < len(l) :
    print(l[i])
    i += 1   


# comprehension(traversing ek line se jyda hota h to bo statement kehlata he , to statement ko single line convert krne ke liye comprehension use krrte he)
copyl = [i/2 for i in 1] #map - manupulation (updation)

copy = [i for i in l if i%2 == 0]  #filter- deletion

print(l)
print (copyl)



#methods in list

l = [1,2,3,4,5,6,7,8,9]
print(dir(l)) # dir se sari method dek skte he

# append (last me ek element add krna)
# extend (last me ek se jyda add krne)
# insert(insert krna only one element)
# "clear","pop","remove","copy","count","index","reverse","sort"

l = [1,2,3,4,5,6,7,8,9]
print(l)
print(dir(l))
print(help(l.extend))

l.append(123)
l.extend([2,4,6,9])
l.insert(3,1234)
print(l)


#"clear","pop","remove"

l.clear()
x = l.pop(2)
print(x)

l.remove(3)
print(l)


# "copy","count","index","reverse","sort"

m = l.copy()
m[1] = 12345
print(m)
print(l)


l.reverse() #reverse the riginal data
l.sort() #sort the original data
l.sort (reverse=True)

print(l.index(21))
print(l.index(21,1,4))
print(l.count(10))

