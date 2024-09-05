# #que38 : accept list element and re print it 
# a = int(input('pls tell how many no you want'))

# l = []

# for i in range(a):
#     z = int(input("pls tell your number"))
#     l.append(z)  

# print(l) 



# #que 39 : print list element in reverse order

# l = [10,20,30,40,50]

# for i in range(len(l)-1,-1,-1):
#     print(l[i])


#que 40: make a list with positive element first than negtive element

# l = [12,-56,89,-34,-78,67,23]

# a = []

# for i in l :
#     if i >= 0:
#         a.append(i)

# for i in l :
#     if i < 0 :
#         a.append(i)

# print(a) 
            



# #que 41: print list ascending and descending order





# #que 42 : Accept size n from user and create a n size List then take n inputs into the and finally Print the sum of all elements in the List in the following manner 10 + 20 + 30 = 60

# n = int(input("how many element you want"))

# l = []

# for i in range(n):
#     z = int(input("tell your numbers"))
#     l.append(z)
 
# sum = 0

# for i in range(len(l)):
#     if i == len(i)-1:
#        print(f"{l[i]} = ",end = " ")
#     else:
#         print(f"{l[i]} + ",end = " ")
#     sum = sum + l[i]

# print(sum)    


 


# #que 43:  Mean of List elements
# a = [1,2,3,4,5]

# sum = 0
# for i in a:
#     sum +=i
# print(f"average is {sum/len(a)}")


# # que 44 :Find the greatest element and print its index too.{2, 96, 69, 77, 145, 20} = Max element = 145 found at 4 index
# a = [2,4,5,20,6,7,8,10]
# max = a[0]
# index = 0

# for i in range (len(a)):
#     if a [i] > max:
#         max = a[i]
#         index = i

# print(f"your max element is at index{index} and value is {max}")     




# # que 45:  Find the smallest element and print its index too.  {2, 96, 69, 77, 145, 20} = Min element = 2 found at 0 index
# a = [2,22,44,43,56,78,1,34,12,64,78,99]
# min =a[0]
# index = 0
# for i in range(len(a)):
#     if a[i] < min:
#         min = a[i]
#         index = i

# print(f"your min element is at index{index} and value is{min}")        



# # que 46: Check if List is sorted or not.
# a = [12,56,23,92,123,78,90]

# max = a[0]
# max2 = a[0]

# for i in a:
#     if i > max:
#         max2 = max
#         max = i
#     elif i > max2:
#         max2 = i    
# print(max2)        




# que 46: Find the second greatest element0 {2, 96, 69, 77, 145, 20} = Second greatest element = 96
#type 1----

# a = [23,67,98,123,45,1,12,14]
# max=a[0]
# max2 = a[0]
# for i in a:
#     if i > max:
#         max2 = max
#         max = i
# print(max2) 

#TYPE --2

# a = [23,67,98,123,45,1,12,14]
# max=a[0]
# max2 = a[0]
# for i in range(len(a)):
#     if a[i] > max:
#         max2 = max
#         max = i
#     elif a[i] > max2:
#         max = a[i]
# print(max2)        



# que 47:    Check if List is sorted or not

# a = [2,4,6,8,10]
# for i in range(0,len(a)-1):
#     if a[i] <= a[i+1]:
#         continue
#     else:
#         print("your list is not sorted") 
#         break
# else:
#     print("your list is sorted")  



#que 48:Pallindromic List :- Write a program to check if elements of an List are same or not it read from front or back Example:arr= [2,3,15,15,3,2]

# a = [1,2,3,3,2,1]

# j = len(a)-1
# for i in range(len(a)//2):
#     if a[i] == a[j]:
#         j -= 1
#         continue
#     else:
#         print("list is not pallindrome")
#         break
# else:
#    print("list is pallindrome")

