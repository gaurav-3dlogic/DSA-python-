def findArraySum(arr,n,b,m):
    n = len(arr)
    i = n - 1
    j = m - 1
    ans = []
    carry = 0
    
    
    while( i >= 0 && j >= 0):
        val1 = arr[i]
        val2 = arr[j]
        
        sum = val1 + val2 + carry
        
        carry = sum / 10
        sum = sum % 10
        ans.append(sum)
        i -= 1
        j -= 1
        
        
    
    
    
    
    