#Tuple is immutable and allows duplicate values.

#1. Creating a tuple
tup = ()
print(tup)
tup = (1,2,3,4,5,6,"Anis","Jord")#using string
print(tup)
li=[1,2,3]#Using List
print(tuple(li))
tup=tuple("Parul University")#built in function
print(tup)

#2. Accessing of Tuples with indexing and slicing
tup=tuple("Vedant")
print(tup[0])#indexing
#SLICING
print(tup[1:5])
print(tup[:3])

#Tuple Unpacking
tup=("Parul","University")
a,b=tup
print(a)
print(b)

#3. Concatenation of Tuples
tup1=tuple("Parul")
tup2=tuple("University")
tup3=tuple(tup1+tup2)
print(tup3)

#Tuples using nested tuples
tup3=(tup1,tup2)
print(tup3)

#4. Deleting a tuple
del tup3
#print(tup3) will throw an error

#Python Tuple Built-in Functions
#1. len():returns the length of the tuple or the size of the tuple.
tupl=(1,2,3)
print(len(tupl))

#2. max():returns the maximum element of given tuple.
tup=(10,20,25)
print(max(tup))

#3. min():returns the minimum element of given tuple.
print(min(tup))

#4. sum():sums up the numbers in the tuple.
tup=(1,2,3)
print(sum(tup))

#5. sorted():input elements in the tuple and returns a new sorted tuple.
tupl=(3,2,1)
print(sorted(tupl))

#6. enumerate():returns enumerate object of tuple/gives index to each element.
tupl=("Parul","University","Vadodra")
for i,name in enumerate(tupl):
    print(f"Index {i}: {name}")

print(list(enumerate(tupl)))