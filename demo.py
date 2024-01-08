def kadaneAlgo(arr):
    sum = 0
    maxSum = 0


    for i in range(len(arr)):
        sum += arr[i]
        maxSum =  max(maxSum, sum)

        if sum < 0:
            sum = 0

    return maxSum

arr = [1,2,-5,8,0]
print(kadaneAlgo(arr)) 