#Find duplicate in an array of N+1 Integers	
#First approach
# a = [1,1,2,3,4,5,5]
# b = []
def find_duplicate(arr):
    res = []


    for i in range(len(arr)):
        if arr.count(i) > 1:
            if i not in res:
                res.append(i)
    if not res:
        return -1
    return res
arr = [1,1,1,1,2,3,4,5]
print(find_duplicate(arr))