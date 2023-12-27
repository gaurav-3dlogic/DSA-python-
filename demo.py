#kadane algo 
def MaxSumSubArray(arr):

    sum = 0
    maxSum = 0

    for i in range(len(arr)):
        sum += arr[i]
        maxSum = max(maxSum, sum)

        if sum  < 0:
            sum = 0

    return maxSum

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(MaxSumSubArray(arr))