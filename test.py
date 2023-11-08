def sort0_1(a,n):

    n = len(a)
    l , m , h = 0 , 0 , n - 1
    while(m <= h):

        if a[m] == 0:
            a[m] , a[l] = a[l] , a[m]
            l += 1
            m += 1
        elif a[m] == 1:
            m += 1
        else:
            a[m] , a[h] = a[h] , a[m]
            h -= 1

    return a

a = [1,2,0,1,0,2,0,1]
n = len(a)
print(sort0_1(a,n))