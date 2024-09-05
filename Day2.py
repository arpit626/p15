#  Que4: Extend the previous program and handle the wrong inputs.
#     Print Good Morning sir for input m or M & Good morning Maam for input F or f 
#    else print Wrong Input



# gender = input ("please tell your gender(M/F):")
# if gender == "M":
#     print = ("Good morning sir ")
# elif gender == "F":
#     print = ("Good morning mam")
# else:
#     print = ("please tell right gender")    


gender = input("Please tell your gender (M/F): ")

if gender.upper() == "M":
   print("Good morning sir")
elif gender.upper() == "F":
   print("Good morning ma'am")
else:
   print("Wrong input! Please enter either 'M' for male or 'F' for female.") 
    
