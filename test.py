arr = [1,3,4,2,10,-5]
target = 5


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

print(pairSum(arr,target))