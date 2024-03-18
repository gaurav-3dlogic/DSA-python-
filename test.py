#pair of sum
a = [1,5,0,2,4,1,3,10,-5]
n = 5

res = []

for i in range(len(a)):
    for j in range(len(a),i+1):
        if a[i] + a[j] == n:
            res.append(a[i],a[j])
print(res)