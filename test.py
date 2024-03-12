
arr = [1,-2,3,-9,10,-3,-5,6,0]

def moveAllN(arr):
    n = len(arr)
    j = 0

    for i in range(n):
        if arr[i] <= 0:
            arr[j],arr[i] = arr[i],arr[j]
            j += 1
    return arr
print(moveAllN(arr))


