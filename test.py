#Find minimum element in list

n = [5,8,4,1,25,6,3]


min1 = n[0]

for i in n:
    if i > min1:
        min1 = i
    
print(min1)