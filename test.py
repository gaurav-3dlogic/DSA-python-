def pair(arr,target):
    num = {}
    pairs = []
    
    
    
    for i in arr:
        c = target - i
        if c in num:
            pair = (c,i)
            pairs.append(pair)
            
        if i in num:
            num[i] += 1
        else:
            num[i] = 1
    return pairs

arr = [1, 5, 7, -1]
target = 6

print(pair(arr,target))