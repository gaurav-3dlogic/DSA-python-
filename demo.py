# def sort01(arr):
#     n = len(arr)
#     l,m,h = 0,0, n -1
#     while m <= h:
#         if arr[m] == 0:
#             arr[l] , arr[m] = arr[m] , arr[l]
#             l += 1
#             m += 1
#         elif arr[m] == 1:
#             m += 1
#         else:
#             arr[m] , arr[h] = arr[h] , arr[m]
#             h -= 1
#     return arr
# arr = [2,1,0,1,0,2,1,2,0]
# n = len(arr)
# print(sort01(arr))
