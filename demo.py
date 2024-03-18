arr = [1,-2,2,1,0,-4]

def kadaneAlgo(arr):
    sum = 0
    maxSum = 0

    for i in range(len(arr)):
        sum += arr[i]
        maxSum = max(maxSum, sum)

        if sum < 0:
            sum = 0
    return maxSum
print(kadaneAlgo(arr))