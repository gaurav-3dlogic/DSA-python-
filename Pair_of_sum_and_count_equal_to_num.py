def findPair(arr,target):
    num = {}
    pairs = []
    

    
    for i in arr:
        c = target - i
        if c in num:
            pair = (i,c)
            pairs.append(pair)
            
        if i in num:
            num[i] += 1
        else:
            num[i] = 1
    return pairs
arr = [1, 5, 7, -1]
target = 6

print(findPair(arr,target))


#count pairs
def count_pairs_with_sum(arr, target):
    num = {}  
    count = 0   
    
    for i in arr:
        c = target - i
        if c in num:
            
            count += num[c]
        
       
        if i in num:
            num[i] += 1
        else:
            num[i] = 1
    
    return count

arr = [1, 5, 7, -1]
target = 6  


print(count_pairs_with_sum(arr, target))