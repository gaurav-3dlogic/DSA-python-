# Extract Unique values dictionary values
a = {"Gaurav":100,"saini":200,"python":500,"java":100}

r = []


for key,value in a.items():
    if value not in r:
        r.append(value)
        
print(r)
    