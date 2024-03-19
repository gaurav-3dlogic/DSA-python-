arr = [1,3,4,2,10,-5]
target = 5
pairs = []
d = {}



def pairOfSum(arr,target):
    for i in range(len(arr)):
        p = target - arr[i]
        if p in d:
            pairs.append(p,[arr[i]])
        else:
            p = arr[i]
    return pairs
print(pairOfSum(arr,target))
