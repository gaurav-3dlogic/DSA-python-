a = [1,2,4,5,6,6]
b = [4,5,6,7,8,6]
c = []

for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)