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

def reverseNum(n):
    if n == 0:
        return 0
    else:
        print(n)
        reverseNum(n-1)
n = 5    
reverseNum(n)