

n = 100

for i in range(2,n):
    
    for j in range(i+1,n):
        if i % j == 0:
            break
    else:
        print(i)
      