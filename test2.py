a = [2,3,4,5,0,1]

n = 5


def pairSum(a,n):
    d = {}
    
    
    for i in range(len(a)):
        p = n - a[i] 
        if p in d:
            return [p,a[i]]
        else:
            d[a[i]] = i 
print(pairSum(a,n))