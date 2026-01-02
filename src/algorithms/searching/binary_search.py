def binary_search(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

arr = [10, 39, 45, 54, 67, 98, 109]
key = 98
print(binary_search(arr, key))