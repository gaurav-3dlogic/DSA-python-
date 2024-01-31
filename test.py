def count_pairSum(arr,target):
    num = {}
    count = 0


    for i in arr:
        c = target - i
        if c in num:

            count += num[c]
        

        if i in num:
            num[i] += 1
        else:
            num[i] = 1
    return count

arr = [1,5,7,-1]
target = 6


print(count_pairSum(arr,target))