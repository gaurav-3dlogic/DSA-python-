arr = [1,2,3,4,6]

def kadaneAlgo(arr):
    maxSum = 0
    sum = 0 
    for i in range(len(arr)):
        sum += arr[i]
        maxSum = max(maxSum, sum)


        if sum < 0:
            sum = 0
    return sum 
print(kadaneAlgo(arr))




