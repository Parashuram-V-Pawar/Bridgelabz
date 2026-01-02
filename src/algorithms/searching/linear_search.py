def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [4, 2, 3, 5, 1]
arr1 = [10, 20, 30, 40, 50]

print(linear_search(arr, 3))  
print(linear_search(arr1, 25)) 