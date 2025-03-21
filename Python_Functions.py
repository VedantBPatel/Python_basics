"""
Functions in python are block of statements that give user ability to to resuse the block of code which ultimately saves from excessive use of memory.
It acts as an time saver and provides better readability of code.
"""

#Craetion of function using def keyword
def greet_user():
    print("Hello user")
    print("Let's learn the use of functions")

def my_func():
    a=0
    for i in range(1,11):
        a=a+i
    return a

greet_user()
print("Sum of first 10 numbers is:",my_func())

#Function with arguments
#1. Default arguments
"""
A default argument is a parameter that assumes a default value if
a value is not provided in the function call for that argument.
"""
def my_func(x,y=50):
    print("x is:",x)
    print("y is:",y)

my_func(10)#default argument

#2. Keyword arguments
"""
A keyword argument allow caller to specify argument name with values
so that caller does not need to remember order of parameters.
"""
def student(firstname,lastname):
    print(firstname,lastname)

student(firstname='Vedant', lastname='Patel')
student(lastname='Patel',firstname='Vedant')

#3. Required arguments
"""
Required arguments are the arguments passed to a function in correct positional order.
They are also known as positional arguments.
If the required argument is not provided, then python will raise an error.
"""

def greet(name, greeting):
    print(f"{greeting} {name}")

greet("Vedant","Hello!")


#4 Variable Length arguments
"""
Vaibale length arguments are the arguments that can also have variable number of arguments.
This can be used when we do not know in advance the number of arguments that will be passed
into a function.
There are two functions provided by python used to allow functions to accept an arbitary number of arguments.
#1. *args:This is used for non keyword arguments,varuable legnth argument list. 
#2. **kwargs:This is used for varialbe length keword arguments.
"""

#1*args
def sum(*args):
    total=0
    for i in args:
        total+=i
    return total

res=sum(1,2,3,4,5)
print("the sum of all numbers is:",res)

#2. **kwargs
def fun(**kwargs):
    for k,val in kwargs.items():
        print(f"{k}:{val}")
fun(name="Vedant Patel", age=20)
#items()function will access both the keys and values of dictionary at the same time.
#without it the loop will only iterate through the keys.

#The Anonymous Functions
lam=lambda a,b:a+b;
print("Value of the function is: ",lam(10,20))
#syntax: 
#variable=lambda arugment1,argument2,argument n:expression/operation