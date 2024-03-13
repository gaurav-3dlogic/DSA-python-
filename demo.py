#Union and interset of two sorted array:-
a = [1,2,3,4,5,4,5]
b = [4,4,5,6,7,7,7]

c = []

for i in a:
    if i not in c:
        c.append(i)
for i in b:
    if i not in c:
        c.append(i)
print(c)
