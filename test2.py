#Kandane Algo
def maxSumarr(arr,n):

    n = len(arr)
    maxSum = 0
    sum = 0

    for i in range(n):
        sum += arr[i]
        maxSum = max(maxSum,sum)


        if sum < 0:
            sum = 0
    return  maxSum
arr = [2,-3,3,2,1,-2,0,-9,1]
n = len(arr)
print(maxSumarr(arr,n))