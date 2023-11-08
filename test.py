


def moveneg(a):
    n = len(a)
    j = 0



    for i in range(n):
        if a[i] < 0:
            a[i] , a[j] = a[j], a[i]
            j += 1
    return a

a = [1,-2,0,8,-1,-2,9,2,4,5]


print(moveneg(a))
