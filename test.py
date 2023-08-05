def sort01(a):
    # n = len(a)
    l = 0
    m = 0
    h = len(a) -1 
    
    
    while(m <= h):
        if a[m] == 0:
            a[m] , a[l] = a[l], a[m]    
            l += 1
            m += 1
        elif a[m] == 1:
            m += 1
        else:
            a[m] , a[h] = a[h] , a[m]
            h -= 1
          
        return a
a = [2,1,0,1,2]    
print(sort01(a))    
        