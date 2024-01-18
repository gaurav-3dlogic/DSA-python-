#map
a = [1,5,2,3]
b = [5,1,2,7]
c = [5,1,2,7]

# def sum(a,b,c):
#     return a + b + c

# res = list(map(sum,a,b,c))

# print(res)


res = list(map(lambda a,b,c : a + b + c,a,b,c))
print(res)
