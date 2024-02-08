a = [10,8,9,-19,9,-2,-1,7]


p , n = 0 , 0

for i in a:
    if i > 0:
        p += 1
    else:
        n += 1
print(p,n)