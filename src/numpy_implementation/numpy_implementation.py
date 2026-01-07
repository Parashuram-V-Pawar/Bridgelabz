import numpy as np

#scalar array
scalar_arr = np.array(12)
print(f"Scalar array: {scalar_arr}")

#One dimensional array
oned_array = np.array([12,34,54,63,12,65])
onedd_array = np.array([12,34,54,63,12,65,89,67])
print(f"One Dimensional array: {oned_array}")
#two dimensional array
twod_array = np.array([[12,43,53],[12,54,65]])
print(f"Two dimensional array:\n{twod_array}\n")
#three dimensional array
threed_array = np.array([[[12,43,54,34],[12,34,78,98]],[[17,1,23,5],[7,56,45,89]],[[24,32,54,34],[12,34,78,67]]])
print(f"Three d array:\n{threed_array}\n\n")

#Indexing or array
arr = np.array([89,56,34,65,76])
print(f"Element at 5th position: {arr[4]}, Element at 3rd position: {arr[2]}\n")

#Array slicing
print("Array slicing: ")
print(f"Positive index slicing: {arr[2:]}")
print(f"Negative index slicing: {arr[:-2]}")
print(f"step slicing: {arr[::2]}")
print(f"step slicing: {arr[::3]}")
print(f"Negative step slicing: {arr[::-2]}\n")

#Array datatypes
int_arr = np.array([23,54,65,34])
float_arr = np.array([1.0, 3, 45, .34])
string_arr = np.array(["Parashu","Vilas","Abin","Sudheer"])
print(f"Array: {int_arr} -> {int_arr.dtype}")
print(f"Array: {float_arr} -> {float_arr.dtype}")
print(f"Array: {string_arr} -> {string_arr.dtype}\n")

#Converting data types
print("Data type conversion in array:")
new_int = int_arr.astype('f')
new_float = float_arr.astype('i')
new_string = int_arr.astype('S')
new_fstring = float_arr.astype('S')
istring = np.array(['2','3','6','8'])
sint = istring.astype('i')
print(f"Original array: {int_arr} -> converted into float: {new_int}")
print(f"Original array: {float_arr} -> converted into int: {new_float}")
print(f"Original array: {int_arr} -> converted into String: {new_string}")
print(f"Original array: {float_arr} -> converted into String: {new_fstring}")
print(f"Original array: {istring} -> converted into int: {sint}\n")

# Copy vs View
print("Copy vs View:")
view = int_arr.view()
print(f"View Before:\nOriginal array: {int_arr} -> view: {view}")
view[2] = 42 
print(f"View After changing element:\nOriginal array: {int_arr} -> view: {view}\n")

copy = new_int.copy()
print(f"copy Before:\nOriginal array: {new_int} -> view: {copy}")
copy[3] = 42 
print(f"copy After changing element:\nOriginal array: {new_int} -> copy: {copy}\n")

# Using shape to check dimension of array
print("Using shape to check the dimension of array: ")
print(f"Scalar Array: {scalar_arr}, shape: {scalar_arr.shape}")
print(f"One dimensional Array: {int_arr}, shape: {int_arr.shape}")
print(f"two dimensional Array: {twod_array}, shape: {twod_array.shape}")
print(f"three dimensional Array: {threed_array}, shape: {threed_array.shape}\n\n")

# Reshaping array
new_int_array = oned_array.reshape(2,3)
print(f"One dimensional Array: {oned_array},\nreshaped array: \n{new_int_array}")
new_3d_array = onedd_array.reshape(2,2,2)
print(f"One dimensional Array: {oned_array},\nreshaped array: \n{new_3d_array}\n")

# Converting multi-dimensional array into 1D array
print(f"3d array converted to 1d: {new_3d_array.reshape(-1)}\n")

# Iterating over arrays
print("Iterating over array using for loop:")
print("1D:")
for x in int_arr:
    print(x)
print("\n2D (element wise):")
for x in twod_array:
    for y in x:
        print(y)
print("\n2D (row wise):")
for x in twod_array:
    print(x)

print("\nEnumerate method: ")
for x in np.ndenumerate(twod_array):
    print(x)


# Joining 2 arrays
print("\nJoining arrays:")
res_arr = np.concatenate((arr, oned_array))
print(f"Array after joining two arrays: {res_arr}\n")

print("Joining 2-D array's")
resd_arr = np.concatenate((twod_array, new_int_array), axis=0)
print(f"{resd_arr}")
# print(np.array_split(int_arr, 5))