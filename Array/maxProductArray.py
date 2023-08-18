def maxProds(arr):
    prod = 1
    maxprod = float("-inf")
    for i in range(len(arr)):
        prod *= arr[i]
        maxprod = max(prod,maxprod)
        if prod == 0:
            prod = 1
    prod = 1
    for i in range(len(arr)-1,-1,-1):
        prod *= arr[i]
        maxprod = max(prod,maxprod)
        if prod == 0:
            prod = 1
            
    return maxprod

arr = [-8,2,3,5]
print(maxProds(arr))
        