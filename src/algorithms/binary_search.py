def binary_search(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if key == arr[mid]:
            return mid
        if key <= arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [78, 54, 67, 34, 76, 87]
key = 67
print(binary_search(arr, key))