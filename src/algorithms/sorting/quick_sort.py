def partition_array(arr, low, high):
    pivot = arr[high]
    i = low -1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1] , arr[j+1] = arr[j+1], arr[i+1]
    return i+1 

def quick_sort(arr, low=0, high=None):
    if high == None:
        high = len(arr)-1
    
    if low < high:
        pivot_index = partition_array(arr, low, high)
        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr,pivot_index +1 , high)

arr = [34,65,78,54,12,42,14,8]
quick_sort(arr)
print(arr)