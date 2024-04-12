
def moba(c):
    return lambda a,b  : a + b + c
res = moba(10)
print(res(5,15))