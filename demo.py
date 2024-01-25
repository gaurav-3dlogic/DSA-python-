list1 = [4,5,4,2,5,63,1,0]
unique_list  = []
for item in list1:
    if item not in unique_list:
        unique_list.append(item)
        
print(unique_list)