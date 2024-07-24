# def find_pair_with_sum(arr, target_sum):
#     arr.sort()  
#     left, right = 0, len(arr) - 1
    
#     while left < right:
#         current_sum = arr[left] + arr[right]
        
#         if current_sum == target_sum:
#             return arr[left], arr[right] 
#         elif current_sum < target_sum:
#             left += 1  
#         else:
#             right -= 1  
    
#     return None  

# arr = [2, 8, 4, 5, 3, 6,-12]
# target_sum = 10
# result = find_pair_with_sum(arr, target_sum)

# if result:
#     print("Pair with sum found:", result)
# else:
#     print("No pair with the given sum")



# #Second Approach

# a = [2,3,4,5,0,1]

# n = 5


# def pairSum(a,n):
#     d = {}
    
    
#     for i in range(len(a)):
#         p = n - a[i] 
#         if p in d:
#             return [p,a[i]]
#         else:
#             d[a[i]] = i 
# print(pairSum(a,n))

#New approach in 2024
# def pairSum(a, n):
#     pairs = []
#     d = {}

#     for i in range(len(a)):
#         p = n - a[i]
#         if p in d:
#             pairs.append([p, a[i]])
#         else:
#             d[a[i]] = i

#     return pairs

# a = [2, 3, 4, 5, 0, 1]
# n = 5
# print(pairSum(a, n))
