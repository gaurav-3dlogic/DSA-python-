#kadane algo
arr = [1,-2,3,4,-6,7,1]

def kadane(arr):
    sum = 0
    maxSum = 0
    for i in range(len(arr)):
        sum +=  arr[i] 
        maxSum = max(maxSum,sum)

        if sum < 0:
            sum = 0
    return maxSum
print(kadane(arr))
