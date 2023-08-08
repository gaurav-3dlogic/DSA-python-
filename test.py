def kadane(a,n):
    n = len(a)
    summ = 0
    maxSum = 0
    
    
    for i in range(n):
        summ = a[i]  + summ 
        
        maxSum = max(maxSum,summ)
        
        
        if summ < 0:
            summ = 0
            
    return maxSum

a = [9,-3,5,0,1,2]
n = len(a)
print(kadane(a,n))