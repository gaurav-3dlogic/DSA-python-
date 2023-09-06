def calculate_median (l1, l2, n):
   i=0
   j=0
   x= -1
   y= -1
   for cnt in range(n+1):
       if i == n:
           x = y
           y = l2[0]
           break
       elif j == n:
           x = y
           y = l1[0]
           break
       if l1[i] < l2[j]:
           x = y
           y = l1[i]
           i = i+1
       else:
           x = y
           y = l2[j]
           j = j+1
   return (x + y)//2

l1 = [1, 12, 15, 26, 38]
l2 = [2, 13, 17, 30, 45]
n = len(l1)

print(calculate_median (l1, l2, n))