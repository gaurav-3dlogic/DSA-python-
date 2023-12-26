a = [1,3,4,6,3]
b = [2,3,4,5,3]

c = []

for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)