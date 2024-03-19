a = [10,3,15,1]



for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            a[i] ,a[j] = a[j],a[i]


print(a)

