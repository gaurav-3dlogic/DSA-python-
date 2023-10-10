a = [4,1,3,2]

m = a[0]


for i in a:
    if i >= m:
        m = i
print("The max number is",m)


for i in a:
    if i <= m:
        m = i
print("The min number is",m)