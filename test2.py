# #Sort01 by using loop

# def sort01(arr):
#     l,m,h = 0,0 , len(arr) -1
#     while m <= h:
#         if arr[m] == 0:
#             arr[m] , arr[l] = arr[l] , arr[m]
#             l += 1
#             m += 1
#         elif arr[m] == 1:
#             m += 1
#         else:
#             arr[h] , arr[m] = arr[m] , arr[h]
#             h -= 1
#     return arr
# arr = [1,2,0,0,1,2]
# print(sort01(arr))