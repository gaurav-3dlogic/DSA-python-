#Move all negitive numbers one side

def moveAllnegitive(arr,n):
    j = 0
    for i in range(0,n):
        if arr[i] > 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1
    print(arr)

arr = [1,-10,9,1,-7,1,-23]
n = len(arr)
print(moveAllnegitive(arr,n))
