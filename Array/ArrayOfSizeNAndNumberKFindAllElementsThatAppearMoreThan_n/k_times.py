def arrayNByK(arr,k):
    # arr = len(arr)
    d = {}
    n = len(arr)
    x = n // k
    res = []
    for i in range(n):
        if arr[i] in d:
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1
    
    
    for i in d:
        if d[i] > x:
            res.append(i)
    return res
    
# def arrayNByK(arr,k):
#     n = len(arr)
#     res = []
#     x= n/k
#     for n in arr:
#         if n >= x and n not in res:
#             res.append(n)
#     return res
        

   



arr = [3, 1, 2, 2, 1, 2, 3, 3]
k = 4
# n = len(arr)

print(arrayNByK(arr,k))