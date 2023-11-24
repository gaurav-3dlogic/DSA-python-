#Binary search program

def binarySearch(arr,l,r,x):
        
    while l <= r:
        mid = l + (r -l) // 2


        if arr[mid] ==  x:
            return mid 
        
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid -1 
    return -1

arr = [2,3,4,10,40]
x = 2

res = binarySearch(arr,0,len(arr) - 1,x)

if res != 1:
    print("Elements is present at index ",res)
else:
    print("Elements is not present in array")

