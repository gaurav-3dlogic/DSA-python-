def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

nums1 = [1, 3, 5, 7, 9, 0, 0, 0, 0, 0]  
m = 5
nums2 = [2, 4, 6, 8, 10]
n = 5

merge(nums1, m, nums2, n)
print(nums1)
# Time Complexity: O(m + n)
# Space Complexity: O(1)
