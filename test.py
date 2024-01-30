#sort list 

a = [4,5,6,7,8,9,10,1,2,3]
c = []


for i in range(len(a)):
    m = a[0]
    for j in a:
        if j < m:
            m = j
    c.append(m)
    a.remove(m)
print(c)


