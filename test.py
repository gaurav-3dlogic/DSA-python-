# Reverse String 
arr = [1,2,3,4,6]

n = arr[0]

m = arr[0]
for i in arr:
    if i < m:
        m = i 
    else:
        n = i 

print(m)
print(n)