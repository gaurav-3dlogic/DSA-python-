from functools import reduce


a = [1,5,2,3,4,5,6,7,8,9,10]


def large(a,b):
    if a < b:
        return a
    else:
        return b
r = reduce(large, a)

print(r)
