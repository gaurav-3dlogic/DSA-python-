# def reveseArray(arr,m):
#     s = m +1 
#     e = len(arr) -1
#     while(s <= e):
#         arr[s],arr[e] = arr[e],arr[s]
#         s += 1
#         e -= 1
#     return arr


# arr = [1,2,3,4,5]

# print(reveseArray(arr,1))

# def reverseNum(n):
#     if n == 0:
#         return 0
#     else:
#         print(n)
#         reverseNum(n-1)
# n = 5    
# reverseNum(n)



# # python code to Check if element exists in list or not

# lst=[ 1, 6, 3, 5, 3, 4 ]
# #checking if element 7 is present
# # in the given list or not
# i=5
# sum = 0
# # if element present then return
# # exist otherwise not exist
# if i in lst:
# 	sum += 1
# print(sum)




def merge(intervals):
    
    x = []
    if len(intervals) == 0:
        return x
    intervals.sort()
    
    temp = intervals[0]
    
    for i in intervals:
        
        if temp[1] >= i[0]:
            temp[1] = max(temp[1],i[1])
            
        else:
            x.append(temp)
            temp = i
    x.append(temp)
    
    
    return x 


intervals = [[0,4],[2,3],[4,1]]
print(merge(intervals))

