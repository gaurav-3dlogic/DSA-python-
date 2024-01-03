def find_duplicate(arr):
    duplicate = []
    n = len(arr)

    for i in range(n):
        index = arr[i] % n
        arr[index] +=  n 

    for i in range(n):
        if arr[i] // n >= 2:
            duplicate.append(i)

    return duplicate

arr = [2,3,4,2,3]
ans = find_duplicate(arr)
for x in ans:
    print(x)