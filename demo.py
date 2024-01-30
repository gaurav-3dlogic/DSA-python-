#sort list

a = [7,8,9,10,1,2,3,4,5,6]
b = []



for i in range(len(a)):
    m = a[0]
    for j in a:
        if j < m:
            m = j
    b.append(m)
    a.remove(m)

print(b)

        






