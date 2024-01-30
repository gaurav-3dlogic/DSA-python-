#longest string

b = "hey gaurav how your love is not pythonww"

a = b.split()

res = ""

for i in a:
    if len(i) > len(res):    
        res = i

print(res)
