def merge(sorted_left, sorted_right):
    final_list = []
    i = 0
    j = 0

    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] < sorted_right[j]:
            final_list.append(sorted_left[i])
            i += 1
        else:
            final_list.append(sorted_right[j])
            j += 1
    
    final_list.extend(sorted_left[i:])
    final_list.extend(sorted_right[j:])    
    return final_list

def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)



arr = [54, 67, 89, 74, 12, 32, 25, 54]
print(merge_sort(arr))