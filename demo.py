a = [1,2,3,4,5,6,7,8,9,10,1]
b = []

for i in a:
    if a.count(i) > 1:
        if i in a and i not in b:
            b.append(i)
print(b)






