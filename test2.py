a = "abc"

def reverseString(arr):
    s , e = 0 ,len(arr) - 1
    arr = list(arr)
    while s < e:
        arr[s] , arr[e] = arr[e] ,arr[s]
        s += 1
        e -= 1
    return ''.join(arr)
print(reverseString(a))