from unittest import result


a = [5,2,1,4,0,2,45,3]

n = 7

#First method
result = [(x,y) for x in a for y in a if x + y == n]

print(result)



#Second method
for x in a:
    for y in a:
        if x + y == n:
            print(x,y)