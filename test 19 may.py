# que 1
a = [2,1,1,2,0,0,1]

for j in range (len(a)-1):
    for i in range(len(a)-1-j):
        if a[i] > a[i+1]:
           a[i],a[i+1] = a[i+1],a[i]

print(a)


#que 2
a = [1,6,6,8,8,9,9,9,10,10]
v = set(a)
print(len(v),list(v)) 

a = [1,6,6,8,8,9,9,9,10,10]

count = 1
j = [a[0]]
for i in range(len(a)-1):
    if a[i] ! = a[i+1]:
            count +=1
            j.append

