"""
So there are some operations like ,creation addition,deletion,updation that can be performed on data types.
String is immutable.
"""

#1: Creating a string
str1= 'Vedant Patel'
print(str1)

str2 = "Vedant"
print(str2)

str3= """This is a multiline
string
"""
print(str3)

#2: Accessing characters 
str = 'Parul University'
print(str[4])
print(str[-12])#negetive index from right

#3: String Slicing/Splitting/Indexing
#substring = s[start : end : step]

s = "Parul University"
print(s[:])#Retrieve all characters
print(s[1:])#Get all characters after a specific position
print(s[1:4])#Extract characters between two positions
print(s[ :4])#Get all characters berfore a specific position
print(s[0:16:2])#Get Characters at specific intervals
print(s[-12:])#negative sliciing 
print(s[:-12])#negative slicing
print(s[-16:-1])#negative slicing 
print(s[::-1])#string reversed
"""
see l's postivie index is 4 and it's also -12 so that is how negative indexing works.
"""

#4: String Updation
"""
Since strings are immutable we can upadte the whole string with a new content,
however we cant replace the characters partially with some others.
"""
str = 'HELLO'
#str[0] = 'h'
print(str)

str = 'hello'
print(str) 


#5: String Deletion
str = 'it is me, your student!'
print(str)
del str
print(str)



#Common String Methods/Functions
#1: len():returns the total number of characters.
str = "Parul University"
print(len(str))

#2: upper():converts all the characters to uppercase
print(str.upper())

#3: lower():converts all characters to lowercase 
print(str.lower())

#4: strip(): removes leading and tailing whitespaces from the string
str = "         Parul University      "
print(str.strip())

#5: replace(): replaces all occurances of a specified substring with anohter.
str= "Parul University"
print(str.replace("Parul", "Rupal"))

#6: title(): Converts the first character to Upper case and others to Lowercase
str = "PARUL UNIVERSITY"
print(str.title())

#7: capitalize(): Converts the first character to Upper case.
str = 'parul university'
print(str.capitalize())

#8: swapcase(): Swaps the cases of all characters in a string.
print(str.swapcase())