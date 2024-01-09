# def mergeTwoSorted(nums1,m,nums2,n):
#     i = m -1
#     j = n -1
#     k = n + m - 1

#     while j >= 0:
#         if i >= 0 and nums1[i] > nums2[j]:
#             nums1[k] = nums1[i]
#             i -= 1
#         else:
#             nums1[k] = nums2[j]
#             j -= 1

#         k -=1 

# nums1 = [1,2,3,4]
# m = 4
# nums2 = [4,5,6,7]
# n = 4
# mergeTwoSorted(nums1, m,nums2,n)
# print(nums1)


#cyclic rotate
def cyclic_rotate(arr):
    n = len(arr)

    last_element = arr[-1]

    for i in range(n-1,0,-1):
        arr[i] = arr[i - 1] 
    
    arr[0] = last_element


arr = [1,2,3,4,5]
cyclic_rotate(arr)
print(arr)
