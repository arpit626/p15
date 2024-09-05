# que 1 : give an integer array nums , return true if any value  

# que 2 given two stirngs ransomNote and magazine, return true if ransomeNote can be constructed by using the letter from magazine and false otherwise.
      # Each letter in magazine can only be used once in ransomNote.
      # eg - 
# que 3 : you have a set of integers s , which riginally contains all the no fron 1 to n . unfortunately , due to some error , one of the no in s got duplicated to another 
        # no in a sets , which result in repetion of one no and loss of another number.
        # you are given an interger array nums representing the data status of this set after th error .
        # find the no  that occur twice and no that is missing and return them in the form of an array.
         # eg: input : nums = [1,2,2,4] 
        #      output: [2,3]
    
        # input: nums = [1,1]
        # output: [1,2]



# 1 
a = [1,2,3,4,5]

d = {}

for i in a:
    if i in d.keys():
        d[i] +=1

        print("true")
        break
    else:
        d[i] = 1

else:
    print("false")


# 2
r = "aa" 
m = "aab"

d1 = {}
d2 = {}

for i in r :
    if i in  d1.keys():
        d1[1] += 1
    else:
        d1[i] = 1    

for i in m :
    if i in  d2.keys():
        d2[1] += 1
    else:
        d2[i] = 1  

for i in d1.key():
    if i in d2.keys():
        if d1[i] <= d2[i]:
            continue
        else:
            print("false")
            break
    else:
        print("true")



# 3
a = [1,2,3,4,5,6,7,7]


for i  in range (len(a)-1):
    if a[i] == a[i+1]:
        print([a[i],a[i+1]+1])




        


