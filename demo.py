# Write a program to cyclically rotate an array by one.	
# def cycle_rotate(arr):
#     n = len(arr)
#     last_element = arr[-1]

#     for i in range(n -1,0,-1):
#         arr[i] = arr[i -1 ]

#     arr[0] = last_element


# arr = [1,2,3,4]
# cycle_rotate(arr)
# print(arr)

#Second Approach
arr = [1,2,3,4]
print([arr[-1]] + arr[0:-1])
