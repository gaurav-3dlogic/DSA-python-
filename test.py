# a = [1,2,3,4,5,6,7,8,9]
# b = [2,3,4,4,6,8,1]


# c = []
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print(c)





def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
 
# Driver Code
lst1 = [1,2,3,4,5,6,7,8,9]
lst2 = [2,3,4,4,6,8,1]
print(intersection(lst1, lst2))