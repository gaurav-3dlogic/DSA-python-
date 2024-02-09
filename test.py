
def pairSum(a,n):
    pairs = []
    d = {}

    for i in range(len(a)):
        p = n - a[i]
        if p in d:
            pairs.append([p,a[i]])
        d[a[i]] = i 
    return pairs

a = [2, 3, 4, 5, 6,0,1]
n = 5

print(pairSum(a,n))
