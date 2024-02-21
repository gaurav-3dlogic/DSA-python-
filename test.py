# def binary_search(arr, target):
    
#     left, right = 0, len(arr) - 1

#     while left <= right:
        
#         mid = (left + right) // 2

#         if arr[mid] == target:
#             return mid
        
#         elif arr[mid] > target:
#             right = mid - 1
        
#         else:
#             left = mid + 1

    
#     return -1

# sorted_list = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
# target_element = 23

# result = binary_search(sorted_list, target_element)
# if result != -1:
#     print(f"Element {target_element} found at index {result}.")
# else:
#     print(f"Element {target_element} not found in the list.")