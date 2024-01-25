# duplicate number in list


a = [1,2,3,4,5,6,1]
res = []


for i in a:
    if a.count(i) > 1:
        if i not in res:
            res.append(i)

print(res)