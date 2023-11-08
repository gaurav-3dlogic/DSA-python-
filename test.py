

def moveneg(a):

    j = 0
    
    for i in range(len(a)):
        if a[i] < 0:
            a[i] , a[j] = a[j], a[i]
            j += 1
        
    return a

a = [7,6,5,0,8,-5,6,-3,2]

print(moveneg(a))