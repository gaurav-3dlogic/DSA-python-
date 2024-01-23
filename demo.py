#reduce example
from functools import reduce 

a = [1,2,3,4,5,6,7,8,9]

def large(a,b):
    if a > b:
        return a 
    else:
        return b
res = reduce(large,a)
print(res)
