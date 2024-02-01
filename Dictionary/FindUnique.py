a = {"Gaurav":100,"saini":200,"python":500,"java":100}

res = []


for key, val in a.items():
    if val not in res:
        res.append(val)
print(res)
