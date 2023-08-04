

def sort012(arr):
    n = len(arr)
    l = 0
    m = 0
    h = n - 1
    
    while m <= h:
        if arr[m] == 0:
            arr[m] , arr[l] = arr[l] , arr[m]
            l += 1
            m += 1
        elif arr[m] == 1:
            m  += 1
        else:
            arr[m] , arr[h] = arr[h] , arr[m]
            m += 1
            h -= 1

        
    return arr

arr = [0,0,2,1,2,1,1,0]
print(sort012(arr))