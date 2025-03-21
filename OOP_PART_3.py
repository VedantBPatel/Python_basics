#Inheritance
"""
Inheritance allows to accquire attributes of already existing parent class into newly created child class.
It provids code reusability.
By using inheritance the child class accquire properties of parent class and can access all the data members and funtions defined in the parent class.
A child class can also provide a specific implementation to the functions of the parent class.
"""
class Person:
    def __init__(self,name):
        self.name=name

    def getName(self):
        return self.name
    
    def isEmployee(self):
        return False
    
class Employee(Person):
    def isEmployee(self):
        return True
    
emp=Person("Rahul")
print(emp.getName(),emp.isEmployee())
emp=Employee("Vedant")
print(emp.getName(),emp.isEmployee())

#Types of Inheritance:
"""
#1. Single Level:
class Animal:
    def __init__(self):
        print("Animal Makes Sound")
    
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog Barks woof wooof")

dog=Dog()
dog.sound()
"""
#2. Multi-Level Inheritance:
"""
class Animal:
   def speak(self):
       print("Animal is speaking")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Puppy(Dog):
    def eat(self):
        print("Puppy eats bread")

d=Puppy()
d.sound()
d.speak()
d.eat()"
"""
"""
#3.Multiple Inheritance:
class Calc1:
    def Addition(self,a,b):
        return a+b

class Calc2:
    def Multiplication(self,a,b):
        return a*b
    
class Derived(Calc1,Calc2):
    def divide(self,a,b):
        return a/b

result=Derived()
print("Divison of two numbers: ",result.divide(10,5))
print("Addition of two Numbers",result.Addition(10,5))
print("Multiplication of two numbers",result.Multiplication(10,5))
#self allows the methods in each parent class (Calc1 and Calc2) to operate on the same instance of Derived."
"""