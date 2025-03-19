#Loops
"""
Loops in progrmming come into use when we need to repeatedly execute a block of statements.
Python supports 3 looping statements that are:
1.For and For-else
2.While and While-else
3.Nested Loops
"""
#1: For and For-else Loop
print("For Loop")
list=["Parul","University","Vadodra"]
for i in list:#List iteration
    print(i)

str="Parul"
for i in str:#string iteration
    print(i)

#for-else
print("\nFor-Else Loop")
"""
else condition is executed only when the loop is not terminated by a break statement.
"""
s="Parul"
for i in s:#Without break
    print(i)
else:
    print("\nNo break")

for i in s:#with break 
    print(i)  
    break
else:
    print("\n No break")
    

#2: While and While-Else Loop
i=0
while(i<3):
    print("Hi")
    i=i+1
else:
    print("Code block inside else and while is executed")
i=0
while(i<3):
    print("Hi")
    i=i+1
    break
else:
    print("Code block inside else and while is executed")

#3: Nested Loops
print("Nested For Loop")
x=[4,5]
y=[1,2]
for i in x:
    for j in y:
        print(i,j)
print("\nNested While Loop")
a=[1,5]
b=[3,2]
i=0
while i < len(a):
    j=0
    while j < len(b):
        print(a[i],b[j])
        j=j+1
    i=i+1
       
    