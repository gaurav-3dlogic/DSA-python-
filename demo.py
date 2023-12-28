#Find duplicate in an array of N+1 Integers	

a = [1,1,2,3,4,5,5]
b = []

for i in range(len(a)):
    if a.count(i) < 1:
        b.append(a[i])
print(b)
    