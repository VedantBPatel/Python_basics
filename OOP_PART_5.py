#Abstraction
"""
Abstraction in python is typically implemented using abstract classes and abstract methods.
Abstract methods provide interface, and subclass must implement them.
It is used to hide the internal functionality of the function from the users.
The users only interact with the basic implementations of the function, but inner working is hidden.
User is familiar with "what a function does" but not with "how it does"
"""
#Abstract Class: Class containing cbstract method.
#Abstract Method: Methods which are defined but not implemented.
#package:abc module:ABC

from abc import ABC,abstractmethod

class Car(ABC):
    def mileage(self):
        pass

class Tesla(Car):
    def mileage(self):
       print("Tesla's mileage is 30km/h")

class Suzuki(Car):
    def mileage(self):
        print("Suzuki's mileage is 25km/h")

t=Tesla()
t.mileage()

s=Suzuki()
s.mileage()

#Encapsulation
"""
Encapsulation allows to bind together data and the functions of a class that operate on them into an single enrity(object).
This puts restictions on accessing variables and methods directly 
and can prevent the accidental modification of data.
To prevent it,, an object's variable can only be changed by an object's method. Those are called private.
"Private variables are variables that are defined within a class and are prefixed with __ to limit their accessibility, ensuring they are only modified or accessed via methods of the class"
"""

class Example:
    def __init__(self, value):
        self.__private_variable = value  # Private variable

    def get_value(self):
        return self.__private_variable  # Accessor method

    def set_value(self, value):
        self.__private_variable = value  # Mutator method

# Instantiate the class
obj = Example(42)
print(obj.get_value())  # Outputs: 42

# Direct access is restricted
# print(obj.__private_variable)  # AttributeError: 'Example' object has no attribute '__private_variable'

# Access via mangled name (not recommended)
print(obj._Example__private_variable)  # Outputs: 42
