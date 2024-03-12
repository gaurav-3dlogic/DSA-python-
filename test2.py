arr = [2,0,1,2,1,2,0]


def sort01(arr):
    low,mid , high = 0 , 0, len(arr) -1 
    while mid <= high:
        if arr[mid] == 0:
            arr[low] , arr[mid] = arr[mid] , arr[low]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid] , arr[high] = arr[high] , arr[mid]
            high -= 1
    return arr
print(sort01(arr))