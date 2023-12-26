#sort 0,1,2


def sort0_1_2(arr):
    low,mid ,high = 0,0,len(arr) -1 
    while mid <= high:
        if arr[mid] == 0:
            arr[mid] , arr[low] = arr[low] , arr[mid]
            low += 1    
            mid += 1
        
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid] , arr[high] = arr[high], arr[mid]
            high -= 1
            
    return arr
arr = [2,0,1,0,2,1,0]   

print(sort0_1_2(arr))