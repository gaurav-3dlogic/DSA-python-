res = [1,2,3,4,5,6,7,8,9,1,2]


for item in res:
    if res.count(item) > 1:
        res.remove(item)
print(res)
