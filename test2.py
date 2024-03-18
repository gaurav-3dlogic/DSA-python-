def pairSum(a,n):
    pair = []
    d = {}


    for i in range(len(a)):
        p = n - a[i]
        if p in d:
            pair.append(pair)
        else:
            d[a[i]] = i
    return pair

a = [2,3,4,5,6,7,8,9,10]
n = 5
print(pairSum(a,n))

