def arrayNByK(arr, k):
    d = {}
    n = len(arr)
    x = n // k
    result = []  # Create a list to store the elements that meet the condition
    
    for i in range(n):
        if arr[i] in d:
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1
    
    for i in d:
        if d[i] > x:
            result.append(i)  # Add the element to the result list
    
    return result  # Return the list of elements that appear more than n // k times

arr = [3, 1, 2, 2, 1, 2, 3, 3]
k = 4
result = arrayNByK(arr, k)
print(result)
