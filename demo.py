def moveNegOneSide(a):

    j = 0
    

    for i in range(len(a)):
        if a[i] < 0:
            a[i] , a[j] = a[j], a[i]
            j += 1

    return a

a = [1,0,-1,3,-4,5,6,-9]
print(moveNegOneSide(a))