#List is mutable and allows duplicate values.

#1: Creating a List
list=[1,2,3,4,5,"Vedant","Rahul"]
print(list)

#2: Accessing List Elements
print(list[0])

#3: Adding Elements into List
"""
In list we can add elements in total 3 ways
1.append():Adds and elements at the end of the list.
2.extend():Adds multiple elements at the end of the list.
3.insert():Adds an element at a specific position.
"""

a=[]
a.append(10)
print("after append(10):", a) 
a.extend([15,20,25,30])
print("after extend():",a )
a.insert(0,5)#insert(index,value)
print("after insert(0,5):",a)     

#4: Updating Elements in Lists
list=[10,15,20,25,30]
list[1]=25
print(list)

#5: Removing Elements in Lists
"""
Just like the addition we can remove the elements in 3 different ways.
1.remove():Removes the first occurence of an element.
2.pop():Removes the element at a specific index or the last element if no index is specified.
3.del:Deletes an element at a spcified index.
"""
list=["Figma","Steve",1,2,3,"Robin","Jack"]
list.remove("Figma")
print( "After removing Figma:",list)
list.pop()
print("After using pop without providing any index",list)
list.pop(2)
print("After providing index to pop(2)",list)
del list[0]
print("After deletion list[0]:",list)
del list
print(list)

#6: Iterating over List
list=["Vedant",1,2,"Josh","David",'s','p','d']
for i in list:
    print(i)
for i in list:
    print(i,end=" ")
print()
#PYTHON LIST METHODS:
#1.copy():Returns a shalow copy of list.
a=[1,2,3]
b=a.copy()
print(b)

#2.clear():Removes all elements from the list.
list=[1,2,3]
print()
print(list)
list.clear()
print(list)

#3.count():Returns the number of times a specified element appeared.
list=[1,2,2,3,4,5,5,5,6,4,8,5,2,54,1,5,5,5]
print(list.count(5))

#4.index():Returns the index of the first occurence of a specified element.
print(list.index(2))

#5.reverse():Reverses the order of the elements in the list.
list=[1,2,3,4,5,6,7,8,9,10]
list.reverse()
print(list)

#6.sort():Sorts the list in ascending order by default.
list.sort()
print(list)