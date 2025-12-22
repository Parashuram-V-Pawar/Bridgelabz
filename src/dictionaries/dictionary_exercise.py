# Creating dictionary
mydict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

dict2 = {
    "color": "red",
    "engine": "V8"
}

# Display dictionary
print("Initial Dictionary:", mydict)

# Length of dictionary
print("Length:", len(mydict))

# Accessing values
print("Brand:", mydict["brand"])
print("Model (using get()):", mydict.get("model"))

# Get all keys
print("Keys:", mydict.keys())

# Get all values
print("Values:", mydict.values())

# Get all key-value pairs
print("Items:", mydict.items())

# Adding new item
mydict["price"] = 5000000
print("After adding price:", mydict)

# Updating value
mydict["year"] = 2024
print("After updating year:", mydict)

# Update using update()
mydict.update({"owner": "John"})
print("After update():", mydict)

# Removing items
mydict.pop("model")
print("After pop('model'):", mydict)

# Remove last inserted item
mydict.popitem()
print("After popitem():", mydict)

# Delete specific key
del mydict["price"]
print("After del price:", mydict)

# Copying Dictionary
copy_dict1 = mydict.copy()
print("Copied dict (copy()):", copy_dict1)

copy_dict2 = dict(mydict)
print("Copied dict (dict()):", copy_dict2)

# Nested Dictionary
nested_dict = {
    "car1": {"brand": "BMW", "year": 2020},
    "car2": {"brand": "Audi", "year": 2022},
    "car3": {"brand": "Tesla", "year": 2024}
}

print("\nNested Dictionary:", nested_dict)

# Access nested value
print("Car2 Brand:", nested_dict["car2"]["brand"])

# Looping Through Dictionary
print("\nLooping Keys:")
for key in mydict:
    print(key)

print("\nLooping Values:")
for value in mydict.values():
    print(value)

print("\nLooping Items:")
for key, value in mydict.items():
    print(key, ":", value)

# Dictionary from Keys
keys = ("name", "age", "city")
newdict = dict.fromkeys(keys, "Unknown")
print("\nfromkeys():", newdict)

# Membership Test
print("\nIs 'brand' in mydict?", "brand" in mydict)
print("Is 'model' not in mydict?", "model" not in mydict)

# Clearing Dictionary
temp_dict = mydict.copy()
temp_dict.clear()
print("\nAfter clear():", temp_dict)
