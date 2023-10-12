# Interesection and union of two sorted array 


def findUnionAndIntersection(arr1,arr2):
    union =  []
    intersection = []
    i,j = 0,0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            union.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            union.append(arr1[j])
            j += 1
        else:
            union.append(arr1[i])
            intersection.append(arr1[i])
            i += 1
            j += 1
        

