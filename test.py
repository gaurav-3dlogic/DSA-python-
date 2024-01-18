a = [1,5,2,3,4,10,12,46]


# def even(a):
#     if a % 2 == 0:
#         return a
    
# res = list(filter(even,a))

# print(res)/


res = list(filter(lambda a: a % 2 == 1,a))
print(res)