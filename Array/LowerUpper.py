a = [2,3,4,5,6,7,8,9,10,11,12]
n = 5


lower = 0
upper = 0


for i in a:
    if i < n:
        lower = i
print(lower)


for j in a:
    if j > n:
        upper = j
        break
print(upper)