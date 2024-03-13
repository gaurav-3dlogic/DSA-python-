#Union and interset of two sorted array:-
a = [1,2,3,4,5,4,5]
b = [4,4,5,6,7,7,7]

c = []

# for i in a:
#     if i not in c:
#         c.append(i)

# for j in b:
#     if  j not in c:
#         c.append(j)
# print(c)

#interset 

for i in a:
    if i in b and not i in c:
        c.append(i)
print(c)

