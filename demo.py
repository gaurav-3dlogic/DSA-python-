# Merge two sorted without using any extra space 

def mergeTwoSorted(arr1,m,arr2,n):
    i = m -1
    j = n -1 
    k = m + n - 1

    while j >= 0:
        if i >= 0 and arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1
arr1 = [1,2,3,4]
m = 4
arr2 = [5,6,7]
n = 3

mergeTwoSorted(arr1,m,arr2,n)
print(arr1)
        

