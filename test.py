#Move all negitive number one side
arr = [1,-2,3,-9,10,-3,-5,6,0]

def moveOneSide(arr):

    j = 0 
    n = len(arr)


    for i in range(n):
        if arr[i] < 0:
            arr[i] , arr[j] = arr[j] , arr[i]
            j += 1
    return arr
print(moveOneSide(arr))
