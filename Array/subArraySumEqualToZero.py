def SubArr(arr,n):
    n = len(arr)
    sumi = 0
    
    
    for j in range(n):
        sumi = arr[j]
        
        if sumi == 0:
            return True
        else:
            for i in range(j+1,n):
                sumi += arr[i]
                if sumi == 0:
                    return True
       
    return False

arr = [4 ,2, -3, 1, 6]
n = len(arr)

print(SubArr(arr,n))        
    
    