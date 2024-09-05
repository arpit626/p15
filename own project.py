#  OOPs in Python

To map with real world scenarios, we started using objects in code.

This is called object oriented programming.


Class & Object in Python

Class is a blueprint for creating objects.

class Student:

name =

“karan kumar”

#creating class

#creating object (instance)

s1 = Student( )
print( s1.name )


Class & Instance Attributes

Class.attr
obj.attr



_ _init_ _ Function

All classes have a function called __init__(), which is always executed when the object is being
initiated.

class Student:

def __init__( self, fullname ):

self.name = fullname

#creating class #creating object

s1 = Student( “karan” )
print( s1.name )

Constructor

*The self parameter is a reference to the current
instance of the class, and is used to access variables
that belongs to the class.

Apna College

Methods

Methods are functions that belong to objects.

class Student:

def __init__( self, fullname ):

self.name = fullname

def hello( self ):
print( “hello”

, self.name)

#creating class #creating object

s1 = Student( “karan” )
s1.hello( )

Apna College

Let‘s Practice

Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average.

Apna College

Static Methods

Methods that don’t use the self parameter (work at class level)

class Student:

@staticmethod
def college( ):

print( “ABC College” )

#decorator

*Decorators allow us to wrap another function in order to
extend the behaviour of the wrapped function, without
permanently modifying it

Apna College

Important

Abstraction

Encapsulation
Hiding the implementation details of a class and only showing the essential features to the user.

Wrapping data an

A
d functions into a single unit (object).