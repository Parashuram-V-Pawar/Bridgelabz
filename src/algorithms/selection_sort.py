def selection_sort(arr):
    size = len(arr)
    for i in range(size):
        min_index = i
        for j in range(i+1, size-1):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr 

arr = [23, 65, 43, 76, 12, 32, 48]
print(selection_sort(arr))  