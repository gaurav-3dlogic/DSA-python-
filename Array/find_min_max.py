# a = [1,5,2,3,4,5]
# a.sort()

# print(a[0],a[-1])



# a = [1,2,4,5,10,3,6,90,-9,-2,0]
# # after sort -- [-9, -2, 0, 1, 2, 3, 4, 5, 6, 10, 90]

# for i in range(len(a)):
#     m = a[0]
#     for j in a:
#         if j >= m:
#             m = j 


# for i in range(len(a)):
#     n = a[0]
#     for j in a:
#         if j <= n:
#             n = j 
# print("The max number is",m)
# print("The min number is",n)


#Second approach
def minMax(a):
    m = a[0]
    n = a[0]
    for i in range(len(a)):
        if a[i] >= m:
            m = a[i]
        elif a[i] <= n:
            n = a[i]
    return("The Max number is",m,"The Min number is",n) 

a = [1,-2,2,3,10,4]
print(minMax(a))