#count pos and neg number

a = [1,2,-2,-9,1,2,-7]
neg,pos = 0,0

for i in a:
    if i < 0:
        neg += 1
    else:
        pos += 1
print(neg,pos)
