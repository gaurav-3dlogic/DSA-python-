#nearest and upper
b = [2, 3, 4, 5, 6,7, 8, 9, 10, 11]
n = 7


lowest = 0
upper = 0


for i in b:
    if i < n:
        lowest = i
print(lowest)


for j in b:
    if j > n:
        upper = j
        break
print(upper)