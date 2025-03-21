#Polymorphism
"""
Polymorphism refers to having muliple forms.
Its a programming term that refers to the use of same method name, but with different signatures, for multiple typles.
"""

class A:
    def show(self):
        print("Inside A")

class B:
    def show(self):
        print("Inside B")

a=A()
b=B()
a.show()
b.show()

#Type os Polymorphism
#1. complie time/polymorphism with class:
class Multiplication:
    def product(self,x,y):
        print("product of {x} {y} is:",x*y)
     
    
    def product(self,x,y,z):
        print("product of {x} {y} {z} is:",x*y*z) 
    
p=Multiplication()
#p.product(2,3)
p.product(2,3,4)

"""
Python doesnt support method overloading, it will simply overwrite the recent one with the previous one.
"""

#2. run time/polymorphism with inheritance:
"""
Run time polymorphism is utilized to achieve method overriding 
in which child class can provide a specific implementation of the method defined in parent class.
The implementation in the child class replaces (overrides) the behavior of the parent class method when called on a child class object.
"""
class Animal:
 def speak(self):
    print("speaking")

class Dog(Animal):
 def speak(self):
    print("Barking")
# Create an instance of Dog and call its speak method
d = Dog()
d.speak()

#Super():The keyword is used to call a method from parent class into child class.
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # Calls the parent class's greet method
        print("Hello from Child")

# Create an instance of Child and call greet
child = Child()
child.greet()
