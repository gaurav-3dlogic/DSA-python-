#Move all the negative elements to one side of the array	

arr = [1,2,-2,1,0,-10,-9,1,7]





def MoveAllNeg(arr):
    nonZero = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[nonZero] , arr[i] = arr[i] , arr[nonZero]
            nonZero += 1


MoveAllNeg(arr) 
print(arr)
            


