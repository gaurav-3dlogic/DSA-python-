def maxSubArr(arr,n):
    maxSum = 0 
    sum = 0
    n = len(arr)
    for i in range(n):
        sum = sum + arr[i]
        maxSum = max(maxSum, sum)
        
        if sum < 0:
            sum = 0
    return maxSum

arr = [1,2,3,4,-1,-2,5]
n = len(arr)
print(maxSubArr(arr,n))