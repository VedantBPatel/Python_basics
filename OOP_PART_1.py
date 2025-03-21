"""
Object Oriented Programming refers to programming pattern that  revolves around object.
"""

#Class
"""
Class is a user defined data type that contains both the data and the functions
that may be used to manipulate them.
Class serves as a blueprint or template to create object.
They provide the characteristics and operations that the object will employ.
"""
#Object
"""
Object is instantiation of Class with unique characteristics and functions. 
Means its a instance of class.
"""
#Creation of Class using class keyword
class Dog:#class
    sound="barks"
dog=Dog()#object
print("Dog",dog.sound)

#What happens when you create an instance for a class?
"""
Whenevere an object is created the __init__ method is invoked/means by default the constructor
is invoked and it initializes the new object and can take arguments to set its unique attributes.
It is basically a instance specific constructor which focuses on initialization of object as needed.
Python by default calls this constructor if not defined manually.
#self: the self keyword is used to specify the instance of a class.
It is a reference to the current instance of the class.
by using self keyword, we can access the attributes and methods of the class in python.
"""

