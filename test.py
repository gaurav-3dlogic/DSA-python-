def threeWayPartition(arr, n, lowVal, highVal):
 
    # Initialize ext available positions for
    # smaller (than range) and greater lements
    start = 0
    end = n - 1
    i = 0
 
    # Traverse elements from left
    while i <= end:
 
        # If current element is smaller than
        # range, put it on next available smaller
        # position.
        if arr[i] < lowVal:
            temp = arr[i]
            arr[i] = arr[start]
            arr[start] = temp
            i += 1
            start += 1
 
        # If current element is greater than
        # range, put it on next available greater
        # position.
        elif arr[i] > highVal:
            temp = arr[i]
            arr[i] = arr[end]
            arr[end] = temp
            end -= 1
 
        else:
            i += 1
    return arr
            
arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]  
lowVal = 14 
highVal = 20     
n = len(arr)    
print(threeWayPartition(arr, n, lowVal, highVal))

#Output: arr[] = {1, 5, 4, 2, 1, 3, 14, 20, 20, 98, 87, 32, 54}