"""
Python Consists total of 5 types of Data types
Numeric(Integer, Complesx, Float)
Dictionary,
Boolean, 
Set,
Sequence(list,tuple,string)
"""

#Numeric Datatype
"""
Immutable.
"""
print("Type of a: ",type(5))
print("\nType of b: ",type(5.2))
c= 4 + 2j
print("\n Type of c: ",type(c))

#Dictionary
"""
This is a key-value pair set arranged in any order. 
It stores specifically value for each key like an associative array or hash table."
It is defined with the curly braces and comma to separate them.
Dictionary in python is mutable and can have duplicate values.
"""
dic1 = {1:"Vedant", 2:"Vrund", 3:"Vivek", 4:"Vishal"}
print(dic1)
print(dic1[1])
print(type(dic1))

#Boolean
"""
It consists of 2 values true and false.
"""
print(type(True))
print(1>2)
print('a'=='a')


#Set
"""
Set in python is unordered collection of data types.
It is defined in curly braces and the elements are separated by comma.
set() function is also used to create an empty set.
Set is mutable and has no duplicate values.
"""
set1=set()
set2={"Vedant","Rohit","Pradyum", "Raj",1,2,3,4}
set3=set("Parul University")
print(set1)
print(set2)
print(set3)


#Sequence Type
#1.String
"""
String in python is characters in the quotation marks.
String in python is immutable but can have duplicate characters.
"""
str1='string using single quote'
str2="string using double quotes"
str3="""A multiline
string
"""
print(str1)
print(str2)
print(str3)

#2.List
"""
List in python is similiar to array in c, however it can have multiple data types.
List is defined in square brackets and elements are separted by comma.
List is mutable and can have duplicate values.
"""
list1=['Vedant',1,2,3,'Rahul']
print(list1)

#3.Tuple
"""
Tuple is an ordered collection of python objects much like this.
Tuple is defined as a record means in small braces and objects are seperated by column.
"""
Tup1=("Vedant", 1,'a','b','z',9)
print(Tup1)
