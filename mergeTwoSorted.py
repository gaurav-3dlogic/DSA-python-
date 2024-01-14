# #First Appraoch

# def merge(nums1, m, nums2, n):
#     i = m - 1
#     j = n - 1
#     k = m + n - 1
    
#     while j >= 0:
#         if i >= 0 and nums1[i] > nums2[j]:
#             nums1[k] = nums1[i]
#             i -= 1
#         else:
#             nums1[k] = nums2[j]
#             j -= 1
#         k -= 1

# nums1 = [1, 3, 5, 7, 9, 0, 0, 0, 0, 0]  
# m = 5
# nums2 = [2, 4, 6, 8, 10]
# n = 5

# merge(nums1, m, nums2, n)
# print(nums1)
# # Time Complexity: O(m + n)
# # Space Complexity: O(1)


# #Second Approach
# def merge(arr1, arr2, arr3):
#     i = j = k = 0
#     n = len(arr1)
#     m = len(arr2)

#     while i < n and j < m:
#         if arr1[i] < arr2[j]:
#             arr3[k] = arr1[i]
#             i += 1
#         else:
#             arr3[k] = arr2[j]
#             j += 1
#         k += 1

#     # Copy the remaining elements of arr1
#     while i < n:
#         arr3[k] = arr1[i]
#         i += 1
#         k += 1

#     # Copy the remaining elements of arr2
#     while j < m:
#         arr3[k] = arr2[j]
#         j += 1
#         k += 1

# def print_array(ans):
#     print(" ".join(map(str, ans)))

# # Example usage
# arr1 = [1, 3, 5, 7, 9]
# arr2 = [2, 4, 6]
# arr3 = [0] * (len(arr1) + len(arr2))

# merge(arr1, arr2, arr3)
# print_array(arr3)

