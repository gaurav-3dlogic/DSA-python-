#Find Largest sum contiguous Subarray [V. IMP]	kadane algo 

def findMaxSubarray(arr):
    sum = 0
    maxSum = 0

    for i in range(len(arr)):
        sum += arr[i]
        maxSum = max(sum, maxSum)

        if sum < 0:
            sum = 0



    return maxSum
arr = [-2, -3, 4, -1, -2, 1, 5, -3]

print(findMaxSubarray(arr))