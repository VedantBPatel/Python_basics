#Constructor
"""
Constructors are generally used for instantiating an object.
The task of constructors is to initialize(assing value)to the data members of the class when an object of class is created.
In python __iniit__ method is called the constructor and is always called when a object is created.
#1.Default Constructor: Which is called implicitly and accepts no arguments.
#2.Parameterized Constructor: Which is called ecplicitly with parameters.
"""
class Animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
        print(f"{name} {sound}")
dog=Animal("dog","barks")
cat=Animal("cat","meows")

#Destructor
"""
Destructors are called whenever an object is destroyed.
The __del__ method is called when all references to the object have been deleted.
"""

class Employee:
    def __init__(self):
        print("Employee Created")

    def __del__ (self):
        print("Employee Deleted.")

emp=Employee()
del emp
