"""
Python provides 2 built in functions to read the input given from the user.
"""
#1.raw input():takes exactly what is typed fromm the keyboard,convert it to string and then return it to the variable in which we want to store.
"""
a = raw_input("Enter your name: ")
print(a)
Above works only in older version of python.
"""

#2. input():This fucntion first takes the input from the user and then evaluates the expression, which means Python automatically identifies whether the user entered a string or a number or list.
a = input("Enter your name : ")
print(a)