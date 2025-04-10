#Python File Handling
"""
File Handling is ability of Python to handle fiels.
To read,write,files along with many other file options.
Python treats files differently as text or binary and this is important.
Each line of code includes a sequence of characters and they form a teext file.
Each line of a file is terminated with a speacial character called the EOL(end of linr)like comaa',' or '\n'
syntax: 
File_Object=open("filename.ext","mode")
File_Object.close()
or
with open("filename.ext","mode")as var:
content inside
no need to close as it will be closed as you are done thanks to with function.
"""
#Basic Handling in Python:
#1.Opening a file:
"""
read():Returns the ready bytes in form of string.
readline():Reads a line of the file and returns it in form of string.
readlines():Reads all the lines and return them as each line a string element in a list.
mode: 
r:to read file
r+:to read and overwrite a file,it will not truncate the data. stream will be at the starting.
"""
"""
with open("samplefile.txt",'r') as f:
    print(f.read())
print()
with open("samplefile.txt",'r+') as f:
    f.write("That")
    print(f.read())
"""

#2. Writing a File:
"""
write():Inserts the string str1 in a single line in the text file.
writelines(): For a list of string elements, each string is inserted in the text file. Used to insert multiple string at a single time.

w:file will get truncated and then the data will be overwritten.
w+:can read and write file/ But existing will be truncated first.
for both stream will be at the starting.
"""

"""
with open("samplefile.txt","w") as f:
   f.write("Hello there!")

with open("samplefile.txt","w+") as f:
    f.write("Hello there user12!")
    f.seek(0)
    print(f.readline())
"""

"""
->The function 'seek(pos)' is used to move the file pointer to a specific position in a file.
It provides precise control over where you want to start reading or writing in the file.
"""


"""
#Some Additional Methods:
#1.Next():It takes the next line everytime it's been called, helpful in loop.
#2.Truncate():This helps in chopping off the file from anywhere to shorten it.
#3.Seek():This function helps users to set the offset position. By default, the value is 0. This is very
useful when someone wants to adjust the position of the reading and writing pointer.
"""