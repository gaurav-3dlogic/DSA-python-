
    


a = [1,5,2,3,4,10,12,46]

#First approach
def even(a):
    if a % 2 == 0:
        return a
        
res = list(filter(even,a))

print(res)

#Second approach
res1 = list(filter(lambda a:a % 2 == 0,a))
print(res1)
