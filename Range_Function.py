"""
range()function in python is used to gernerate a serires of numbers within a given range.
Depending on how many arguements the user is passing to the function.
User can decide from where to start, stop and how many steps.
syntax: range(start,stop,step)
"""
for i in range(5):
    print(i)
print()
print("two arguments")
for i in range(0,5):
    print(i)
print()
print("three arguments")
for i in range(0,10,2):
    print(i)