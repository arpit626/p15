
# loop variable
# condition expression 
# updation expression
#  body of loop

# two types of loop 
#1 entry control loop(while loop , for loop)
#2 exist control loop(do while loop)
# in python doen not have exist control loop


# loop variable
# while (condition_exp);
#    body of loop
#    updation expression

#i = 1
#while i <=10:
 #   print(i)
  #  i += 1
#print("End of while loop")   


# we can directly use sequential and non seq datatypes in for loop
#we dont know no of iteration of loop when using while loop
# when know no of iteration of loop when using for loop

#we can define range in three form
#1 range (start, end + 1 , update)
#2 range (start, end + 1) by default update = 1
#3 range (end+1) by default start = 0, update = 1


#for i in range (1, 11 , 2): 
#  print (i) 
#for i in range (11 , 1 , -1):
#  print (i)

# // sunday class: 17 march //

# break
# continuous
# else 



#1 continue
#n  = 10
#while n>= 1:
    
   # n -= 1
   # if n == 5:
        
   #     continue # skip the code below the statement and move the control towards updation expreession
    
   # print(n)


#2 break
n  = 10
while n>= 1:
    
    n -= 1
    if n == 5:
        
       break # stop the loop and take the control out of the loop
    print(n)

# this is run after the break    
    

 #3 else  
n  = 10
while n>= 1:
    
    n -= 1
    if n == 5:
        
       continue
    print(n) 
else:                     # only else work in continue they do not work with break
    print("else ran...")   


#pass ka use jb krte hain jb hume output ki jrurt nhi ho , use khali nhi chor skte kuki error aayega
n  = 10
while n>= 1: 
    
    pass

if n % 2 == 0:
    pass
else:
    print("hellow")