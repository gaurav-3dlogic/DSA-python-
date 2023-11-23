#Binary Search
def BinarySearch(arr,l,r,x):
    

    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid
    
        elif arr[mid] < x:
            l = mid + 1

        else:
            r = mid - 1
        
    return -1

arr = [3,1,4,5,2,6,78]
x = 3
res = BinarySearch(arr,0,len(arr) -1,x)
if res != -1:
    print(res)
else:
    print("Array is not binary search")


