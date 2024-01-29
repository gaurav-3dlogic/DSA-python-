# n = 6
# a = []


# while(n > 0):
#     dig = n % 2
#     a.append(dig)
#     n = n // 2


# a.reverse()
# for i in a:
#     print(i, end= "")


list1 = [3,1,2,3,5]


for item in list1:
    if list1.count(item) > 1:
        list1.remove(item)
print(list1)