tuple1 = (12,9,32,16,45,20,54,76)
tuple2 = ("apple","strawberry","banana","cherry","raspberry","mango")

# "Printing tuple"
print(tuple1)
print(tuple2)

# "Printing Length of tuple"
print(len(tuple1))
print(len(tuple2))

# "Printing only required value using indexes"
print(tuple1[4])
print(tuple2[5])
print(tuple1[2])

# "Using loops to print all values in tuples"
print()
for i in tuple1:
  print(i)
print()
i=0
while i<len(tuple2):
  print(tuple2[i])
  i +=1
print()
# "accessing elements using a given range in tuple"
print(tuple1[1:5])
print()


# "updating a tuple"
mylist = list(tuple1)
mylist[1] = "Fruit"
tuple1 = tuple(mylist)
print(tuple1) 

mylist = list(tuple1)
mylist.remove(16)
tuple1 = tuple(mylist)
print(tuple1)

# "Unpacking a tuple"
(green, yellow, red, blue, pink, brown) = tuple2
print(green)
print(yellow)
print(red)
print(blue)
print(pink)
print(brown)

print("\n\n")
(bike, car, *bus) = tuple2
print(bike)
print(car)
print(bus)