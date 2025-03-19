"""
Python Set is unordered, mutable and it will by default igonre duplicate objects.
"""
#Creating a Set
a=set()
print(a)
a.add((5,6,7,8))#adding a tuple
print(a)
a.update([9,10,12,11])#update with a list
print(a)

#Accessing a set
a=set(["Parul","University","Vadodra"])
for i in a:
    print(i,end=" ")
print()
#Removing Elements
#1. remove():removes the element in the set if only it is present in the set otherwise throws and exception
a.remove("Parul")
print(a)
 
 #2. discard(): discards the elements in the set if only it is present and if not then nothing happens and the exception is not thrown.
a.discard("Vadodra")
print(a)

#3. clear():removes all the elements of the set
s={1,2,3,4,5,6,7}
print(s)
s.clear()
print(s)

#additional set methods
#1. union():returns the unique values
set1={1,2,3,4,5,6,7,8,9,10}
set2={4,5,6,7,8,9,10}
print(set1.union(set2))

#2. intersection():returns the common values
print(set1.intersection(set2))

#3. difference():return the minused value
print(set1-set2)