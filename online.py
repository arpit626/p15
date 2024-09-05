#prime numbers -  A prime number is defined as a natural number greater than 1 and is divisible by only 1 and itself.
# Que: prime numbers in a range

a = int(input("from where you want to start"))
n = int(input("till where you want to go"))
countprime = 0
for i in range(2,n+1):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count = count + 1 
    if count == 2:
        countprime+=1 

print(countprime)       


# what is strong numbers - A strong number is a positive integer whose sum of factorials of its digits equals the number itself. 
                           #In other words, if we take the digits of a number and calculate the factorial of each digit, 
                           #then sum those factorials, and the result is the same as the original number, then that number is called a strong number.

# For example, 145 is such a number because 1! + 4! + 5! = 1 + 24 + 120 = 145. Similarly, 40585 is also a type of number because 4! + 0! + 5! + 8! + 5! = 24 + 1 + 120 + 40320 + 120 = 40585.

 # strong numbers 

n = int(input("please tell a number"))
copy = n
sum = 0
while n > 0:
    fact = 1
    for i in range(1,(n%10)+1):
        fact = fact * i

    sum = sum + fact   
    n = n//10

if sum == copy:
    print("bhai aapka number strong hai ")
else:
    print("nahi hai strong")    


# armsrong number -  An Armstrong number (also known as a narcissistic number, plenary number, or pluperfect digital invariant)
# is a number that is equal to the sum of its own digits each raised to the power of the number of digits. 
#For example, 153 is an Armstrong number because:
#  1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 



# armstrong number

def is_armstrong(num):
    # Count number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Compute the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit)**num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return armstrong_sum == num

# Example usage
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")