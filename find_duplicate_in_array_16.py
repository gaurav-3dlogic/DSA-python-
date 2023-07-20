def duplicates(arr, n): 
    r = []
        
    for i in arr:
        if arr.count(i) > 1:
            if i not in r:
                r.append(i)
    
    if not r:
        return -1
    return r

arr = [2, 3, 1, 2, 3, 0, 0]
n = len(arr)

print(duplicates(arr, n))






# def find_duplicate(arr, n):
#     seen = set()
    
#     for i in range(n):
#         if arr[i] in seen:
#             return arr[i]
#         else:
#             seen.add(arr[i])

#     return -1
  
  
# arr = [1,2,2,3,3]
# n = len(arr)
# print(find_duplicate(arr,n))