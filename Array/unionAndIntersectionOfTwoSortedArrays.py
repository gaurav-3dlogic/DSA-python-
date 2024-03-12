# def find_union_and_intersection(arr1, arr2):
#     union_result = []
#     intersection_result = []
#     i, j = 0, 0

#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             union_result.append(arr1[i])
#             i += 1
#         elif arr1[i] > arr2[j]:
#             union_result.append(arr2[j])
#             j += 1
#         else:
#             union_result.append(arr1[i])
#             intersection_result.append(arr1[i])
#             i += 1
#             j += 1

  
#     while i < len(arr1):
#         union_result.append(arr1[i])
#         i += 1
#     while j < len(arr2):
#         union_result.append(arr2[j])
#         j += 1

#     return union_result, intersection_result


# arr1 = [1, 3, 4, 5, 7]
# arr2 = [2, 3, 5, 6]
# union_result, intersection_result = find_union_and_intersection(arr1, arr2)
# print("Union:", union_result)
# print("Intersection:", intersection_result)

#Time complexity 0(m + n)
#Space complexity 0(1)


a = [1, 2, 4, 5, 6, 6]
b = [4, 5, 6, 7, 8, 6]
c = []
d = []

#Union 
for i in a:
    if i not in c:
        c.append(i)
for i in b:
    if i not in c:
        c.append(i)
print(c)

#Interset
for i in a:
    if i in b and i not in d:
        d.append(i)
print(d)
