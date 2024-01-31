from unittest import result
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 7

result = [(x,y) for x in a for y in a if x + y == n]

print(result)


# for x in a:
#     for y in a:
#         if x + y == n:
#             print(x,y)




