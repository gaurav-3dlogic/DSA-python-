def pairSum(arr,target):
    pairs = []
    d = {}

    for i in range(len(arr)):
        p = target - arr[i]
        if p in d:
            pairs.append([p,arr[i]])
        else:
            d[arr[i]] = i
    return pairs

arr = [5,1,4,3,7,8,9,3,21,2,6,5,4]
target = 8
print(pairSum(arr, target))
