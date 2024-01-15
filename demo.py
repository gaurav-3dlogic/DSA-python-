def reverse_arr(arr):
    s,e = 0 , len(arr) -1 
    while s < e:
        arr[s] , arr[e] = arr[e] , arr[s]
        s += 1
        e -= 1
    return arr
arr = [2,3,4,5]
print(reverse_arr(arr))