n = 7
res = []




while n > 0:
    dig = n % 2
    res.append(dig)
    n = n // 2

res.reverse()

for i in res:
    print(i,end = "")