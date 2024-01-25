list1 = [1,2,3,4,5,6,7,8,9,10,11,12,1,2]

for i in list1:
    if list1.count(i) > 1:
        list1.remove(i)
print(list1)


