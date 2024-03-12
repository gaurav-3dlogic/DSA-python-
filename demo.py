arr = [1, 2, 4, 5, 6]


def cyclic(arr):
    n = len(arr)
    last_ele = arr[-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = last_ele

cyclic(arr)
print(arr)