arr = [1,2,5,10,3,-5,4]
target = 5
def sortList(arr,target):
    pairs = []
    d = {}
    for i in range(len(arr)):
        p = target - arr[i]
        if p in d:
            pairs.append([p,arr[i]])
        else:
            d[arr[i]] = i
    return pairs
print(sortList(arr,target))
