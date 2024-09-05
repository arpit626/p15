# 12 june class
# # OOPS Day 1 notes


# PPP(Procedural Programming Paradigm)
# In this, we write the code in a sequence of steps. It is a top-down approach. It increases the lines of code and decreases the reusability of the code.


# OOPS(Object-Oriented Programming Paradigm)
# In this, we write the code in the form of classes and objects. It is a bottom-up approach. It increases the reusability of the code and decreases the lines of code. It encapsulates the data and functions. It has security.


#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

# OOPS Concepts



# 5. Class & Object
# Class is a blueprint of an object. It is a user-defined data type. It is a collection of objects. It is a template of an object. It is a logical entity. It is a reference data type.
# Object is an instance of a class. It is a real entity. It is a physical entity. It is a memory entity. It is a value data type.
# Object is an instance of a class. It is a real entity. It is a physical entity. It is a memory entity. It is a value data type.

class Factory:
    a = 12 #(If this is defined inside of the class it is called as attribute)
    # __a = 12 #(If this is defined inside of the class it is called as private attribute)
    # _a = 12 #(If this is defined inside of the class it is called as protected attribute)
    # __ we can put this before function also like __hello() and it is called as private function

    def hello():
        print("Hello")

a = 23 #(If this is defined outside of the class it is called as variable)

def hello():   # This is a function in which a is a global variable which can be accessed from anywhere
    global a
    print(a)

# hello()

# print(Factory.a) # This is a class attribute which can be accessed by the class name


# Let's make an object
# Object are only made when you call the class, it can access all items of a class which makes it a child in a way

obj = Factory()

# print(obj.a)

# Constructor

class Factory:
    def __init__(self,BT,T,ET):  # This is a constructor, in this "self" is a reference to the object or the class itself
        self.BodyType = BT
        self.Tyres = T
        self.EngineType = ET

    def show(self):
        print("your car has: ")
        print(f"1. {self.Bodytype} bodytype") 
        print(f"2. {self.Tyres} as tyres") 
        print(f"3. {self.Enginetype} as Engine ") 

    def mountain(self):
        if int(self.Enginetype[0]) >= 8:
            print ("your vehicle can climb mountain")
        else:
            print("your vehicle can not climb mountain ")    

Ferarri = Factory("Covered",4,"8-Cycle")
Lord_Alto = Factory("Covered",4,"4-Cycle")
Splender = Factory("Open",2,"6-Cycle")

Ferarri.mountain()


# 14 june class
# day 2 (backup)

# Oops Project(taking admission in school)
# Que = craete a registeration form for taking addmission in twelth class if percentage above 50 
class Twelth:
    def __init__(self,percentage):
        if percentage < 50:
            self.percentage = percentage
            self.admission = True
        else:
            print("sorry you can not register yourself")
            self.admission = False
    
    @property
    def admission (self):
        if self.admission == True:
            print("yes you are admitted to our school")
        else:
             print("yes you are not admitted to our school")   

arpit  = Twelth(47.9) 
vikas = Twelth(80)               

arpit.admission()




# magic method (dunder method)

class Animal:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name
     
animal1 = Animal("lion")        
animal2  = Animal("Giraffe")        
animal3  = Animal("Fox")        


print(animal1)



# add magic method
class number:
    def __init__(self,num):
        self.num = num

    def __add__(self, num2):
        return self.num + num2.num

    def __eq__(self,Object):
        print(self.num == Object.num)

# n1 = number(int(input("Enter the number : ")))
# n2 = number(int(input("Enter the number : ")))

n1 = number(4)
n2 = number(5)


# repr magic method
class String: 
      
    def __init__(self, string): 
        self.string = string 
          
    def __repr__(self): 
        return 'Object: {}'.format(self.string) 
  
if __name__ == '__main__': 
      
 
    string1 = String('Hello')  
    print(string1) 



# 16 june class
#  day 3 (backup)

# OOPS Day 2 notes - Polymorphism

class Animal:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(self.name)

class Human:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(self.name)


obj1 = Animal("Lion")
obj2 = Human("Utkarsh")

# obj1.show()
# obj2.show()


# Inheritance
# Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).

# Below is an exampple of "Single Level Inheritance"

class Reebook:
    def __init__(self,zips,pockets,material):
        self.zips = zips
        self.pockets = pockets
        self.material = material

    def show(self):
        print("Your bag has",self.zips, self.pockets, self.material)


class Hrx(Reebook):    # This is an example of inheritance
    def __init__(self,zips,pockets,material,laptop):
        super().__init__(zips,pockets,material)      # Super function is used to call the parent class constructor
        self.laptop = laptop

    def show(self):   # This is an example of method overriding, because the method is already present in the parent class but we are defining it again in the child class
        print("Your bag has",self.zips, self.pockets, self.material, self.laptop)

class Zara(Hrx):   # This is an example of Multilevel Inheritance, as Zara is inheriting from Hrx and Hrx is inheriting from Reebook
    def __init__(self, zips, pockets, material, laptop, wp):
        super().__init__(zips, pockets, material, laptop)
        self.wp = wp

    def show(self):
        print("Your bag has",self.zips, self.pockets, self.material, self.laptop, self.wp)

bag1 = Reebook(2,3,"Leather")
bag2 = Hrx(3,4,"Cloth","Yes")
bag3 = Zara(4,5,"Plastic","Yes","Yes")

# bag1.show()
# bag2.show()
# bag3.show()


# Abstraction
# Abstraction is the concept of hiding the complex implementation or hiding unecessary details from the user. 

# Below is an example of Abstraction

from abc import ABC, abstractmethod

class Area(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class square(Area):
    def __init__(self,side):
        self.side = side

    def show(self):
        print("Side of the square is",self.side)

    def area(self):
        pass

    def perimeter(self):
        pass


area1 = square(5)    