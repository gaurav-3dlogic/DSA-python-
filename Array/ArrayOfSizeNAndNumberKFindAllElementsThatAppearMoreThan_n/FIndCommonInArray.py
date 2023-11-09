# def find_common_elements(array1, array2):
#   common_elements = []
#   for element1 in array1:
#     for element2 in array2:
#       if element1 == element2:
#         common_elements.append(element1)
#   return common_elements

# array1 = [1, 2, 3, 4, 5]
# array2 = [2, 3, 4, 6, 7]

# common_elements = find_common_elements(array1, array2)
# print(common_elements)


a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 6, 7]
c = []

for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)