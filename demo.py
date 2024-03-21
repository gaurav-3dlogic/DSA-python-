arr = [1,2,5,10,3,-5,4]
target = 5
def sortList(arr,target):
    pairs = []
    d = {}
    for i in range(len(arr)):
        p = target - arr[i]
        if p in pairs:
            pairs.append([p,arr[i]])
        else:
            d[arr[i]] = i
print(sortList(arr,target))
