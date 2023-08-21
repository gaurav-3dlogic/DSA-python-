def findLongestConseqSubseq(arr, N):
    ans = 0
    count = 0
    
    arr.sort()
    
    v = []
    v.append(arr[0])
    
    
    for i in range(1,N):
        if (arr[i] != arr[i -1]):
            v.append(arr[i])
    for i in range(len(v)):
        
        if(i > 0 and v[i] == v[i-1] + 1):
            count += 1
        else:
            count = 1
            
        ans = max(ans,count)
    return ans

N = 7
arr = [2,6,1,9,4,5,3]

print(findLongestConseqSubseq(arr, N))