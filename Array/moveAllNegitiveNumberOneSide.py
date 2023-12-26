def moveNegOneSide(a):
    
    j = 0   
    n = len(a)
    
    
    for i in range(n):
        if a[i] < 0:
            a[i] , a[j] = a[j], a[i]
            j += 1
    return a 


a = [1, -1, 3, 2, -7, -5, 11, 6]
print(moveNegOneSide(a))        