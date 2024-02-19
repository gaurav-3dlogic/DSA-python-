def binary(arr,target):
    left,right = 0 , len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid 
        
        elif arr[mid] > target:
            right = mid - 1
        
        else:
            left = mid + 1
    return -1
sorted_elems = [1,2,3,4,5,6,7,8,9,23,24,25,26,27,28]
target = 8
result = binary(sorted_elems, target)
if result != -1:
    print(f"Element {sorted_elems} found at index {result}.")
else:
    print(f"Element {sorted_elems} not found in the list.")