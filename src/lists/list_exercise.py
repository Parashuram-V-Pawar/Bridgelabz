# function to support customize sort
def myfunc(n):
  return abs(n-50)


# Creating lists
mylist = [12, 7, 5, 64, 50, 14]
list2 = ["Apple","banana","Cherry","dates"]

# Displaying list elements
print(mylist)

#Displaying length of list
print(len(mylist))

# Adding Elements
mylist.append(23)
print('Added 23: ',mylist)
mylist.insert(2,33)
print("added 33 at position 3: ",mylist)

# Removing elements
mylist.remove(14)
print("removed 14: ",mylist)
mylist.pop(3)
print("removed element at index 3: ",mylist)

# List Comprehension
newlist = [x for x in list2 if "a" in x]
print("List Comprehension: ",newlist)

# clearing list
newlist.clear()
print("newlist: ",newlist)

# Sorting
mylist.sort()
print(mylist)
list2.sort()
print(list2)

# customizing sort function
mylist.sort(key=myfunc)
print(mylist)

# reverse list
mylist.reverse()
print(mylist)
list2.reverse()
print(list2)


# Copying Lists
newlist2 = mylist.copy()
print("Copied List(using copy()): ",newlist2)

newlist3 = list(list2)
print("Copied List(using list()): ",newlist3)

newlist4 = mylist[:]
print("Copied List(using slice[:]): ",newlist4)


# Join Lists
print("Join List:")
newlist5 = mylist + newlist4
print("Using + operator: ",newlist5)

for x in list2:
  newlist2.append(x)
print("Using append(): ",newlist2)

newlist3.extend(newlist4)
print("Using extend(): ",newlist3)