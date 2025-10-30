def merge_sort_and_count(arr):
    if len(arr) <= 1:
        return 0

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    inversions = 0
    inversions += merge_sort_and_count(left_half)
    inversions += merge_sort_and_count(right_half)

    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
            inversions += (len(left_half) - i)
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
        
    return inversions

my_list = [4, 3, 2, 1]
total_inversions = merge_sort_and_count(my_list)

print(f"Lista ordenada: {my_list}")       
#print(f"Total de inversiones: {total_inversions}") 
