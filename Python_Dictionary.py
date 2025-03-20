"""
Python Dictionary is a unordered collection of data values, used to store data values like  a map.
It holds key:value pair.
Each key-value pair is separted by comma. and is braced under curly braces.
Dictionary is mutable and it values can be duplicated by key must be unique.
"""
#1. Creating a dictionary
dic1 = {1:'Vedant',2:'Rahul',3:'Jay',4:'Mohit'}
print(dic1)

#2. Accessing Elements from dictionary
print(dic1[2])
print(dic1.get(3))

#3. Updating Elements in dictionary
dic1[2] = 'Roman'
print(dic1)
#dic1.update(2='rocky')

#4. Adding Elements in dictionary
dic1[5]='Ronin'
dic1[6]='Jack'
dic1[7]='James'
print(dic1)
"""
So the logic here is that we will have to manually add each key-value pair as we have taken numbers as our key
and in python variable naming rules are strictly against it ,
there is a function dict() which follows this rule so if we want to  add int key we have to do it manually.
"""
myDict = {'a': 1, 'b': 2}
newDict = dict(myDict, d=4)  # Output: {'a': 1, 'b': 2, 'd': 4}
print(newDict)

myDict = {'a': 1, 'b': 2}
newdict = dict(myDict)
newdict[5] = 'e'  # Manually adding a key-value pair
print(newdict)

#5.Removing Elements from dictionary
print("before removing",dic1)
dic1.pop(5)#using pop()
print("after removing", dic1)

dic1.popitem()#popitem() works like in fifo stack, means it removes the last recent
print(dic1)

del dic1[6]#using delete
print(dic1)

dic1.clear()
print(dic1)