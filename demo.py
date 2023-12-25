#Find the max and min number in array

# a = [4,1,2,5,5]
# a.sort()
# print(a[0],a[-1])



arr = [4,1,2,5,5]
m = arr[0]
for i in arr:
    if i >= m:
        m = i
n = arr[0]
for j in arr:
    if j <= n:
        n = j
print("max",m)
print("min",n)
  
    
  
