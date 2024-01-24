#possible substring

a = "abc"
res = []


for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        res.append(a[i:j])

print(','.join(res))