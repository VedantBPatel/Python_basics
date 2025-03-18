a=9
b=4

#Arithmetic Operators

#Addition
add=a+b
#Subtraction
sub=a-b
#Multiplication
mul=a*b
#Division(float)
div1=a/b
#Division(floor)
div2=a//b
#Modulo
mod=a%b

print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(mod)


#Relational Operators
a=13
b=33

#Greater than 
print(a>b)

#Less than
print(a<b)

#Equals to
print(a==b)

#Not equal to
print(a!=b)

#Greater than or Equal to
print(a>=b)

#Less than or Equal to
print(a<=b)

#Logical operators
a=True
b=False

print(a and b)#prints a and b is false
print(a or b)#prints a or b is true
print(not a)#prints not a is false


#Bitwise Operator
a=10
b=4
print(a & b )#and
print(a | b)#or
print(~a)#complement
print(a ^ b)#xor
print(a>>2)#right shift
print(a<<2)#left shift

#Python has additional 2 operators: membership and identity
a=15
b=10
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#membership operators
if(a in list):
    print(f"{a} is present in list")
else:
    print(f"{a} is not present in list")

if(b not in list):
    print(f"{b}is not present in list")
else:
    print(f"{b} is present in list")


#identity operators
print(a is 15)
print(a is not 15)