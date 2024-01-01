#Kadane alogrithm

def kadane(arr):
    sum = 0
    maxSum = 0
    for i in range(len(arr)):
        sum += arr[i]
        maxSum = max(sum, maxSum)

        if sum < 0:
            sum = 0



    return maxSum

arr = [1,2,5,-4,6,1]
print(kadane(arr))
