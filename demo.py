list1 = [4,1,5,2,4,5]



for item in list1:
    if list1.count(item) > 1:
        list1.remove(item)
print(list1)