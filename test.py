arr = [1,2,3,4,6]


def cyclic(arr):
    last_ele = arr[-1]
    n = len(arr)
    for i in range(n-1,0,-1):
        arr[i] = arr[i - 1]
    arr[0] = last_ele
cyclic(arr)
print(arr)

