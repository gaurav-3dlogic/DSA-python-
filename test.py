
a = [1,2,3,5,6]

def cyclic(arr):
    last_ele = arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i] = arr[i - 1]
    a[0] = last_ele

    return arr
cyclic(a)
print(a)
