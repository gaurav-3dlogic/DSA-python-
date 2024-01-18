a = [1,5,2,3]
b = [5,1,2,7]

#First approach
def sum1(a,b):
    return a + b
    
result = list(map(sum1,a,b))
print(result)

#Second approach
result1 = list(map(lambda a,b : a+b ,a,b))
print(result1)