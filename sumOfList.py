#First approach
a = [1,2,3,4,5,6,7,8,9,10]
# res = 0

# for i in a:
#     res += i
# print(res)


#Second approach
from functools import reduce
def SumNum(a,b):
    return a + b

print(reduce(SumNum,a))


