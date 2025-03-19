#Decision making
"""
In python conditional statements are used to control the flow of the execution based on cerain conditions.
There are 4 types of statements in python.
1.if
2.if-else
3.nested if
4.if-elif ladder
"""

#1: If Statement
a = 10
b = 15

if a%2==0:
    print("Even Number")

#2: If Else staement
a = 10
b = 15

if b%2==0:
    print("Even Number")
else:
    print("Odd Number")


#3: Nested If
a=10
if a%2==0:
    if a%5==0:
        print("a is divisible by both 2 and 5")


#4: If-Elif Ladder
a=10

if a==11:
    print("a is 11")
elif a==10:
    print("a is 10")
else:
    print("a is not present")