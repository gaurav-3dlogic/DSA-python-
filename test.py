def movenNegitiveOneSide(a):
    j = 0
    n = len(a)

    for i in range(n):
        if a[i] < 0:
            a[i] , a[j] = a[j], a[i]
            j += 1
    return a

a = [1,2,3,-1,0,-9,-2,-4,8,4]

print(movenNegitiveOneSide(a))