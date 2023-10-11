def sort01(arr,n):
    l,m,h = 0,0,len(arr) -1
    while(m <= h):
        if(arr[m] == 0):
            arr[m] , arr[l] = arr[l] , arr[m]
            m += 1
            l += 1
        elif(arr[m] == 1):
            m  += 1
        else:
            arr[m] , arr[h] = arr[h] , arr[m]
            h -= 1

    return arr
arr = [2,1,0,2,1,0,1,0]
n = len(arr)
print(sort01(arr,n))
    