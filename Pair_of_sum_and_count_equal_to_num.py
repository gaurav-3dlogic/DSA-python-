def findPair(arr,target):
    num = {}
    pairs = []
    

    
    for i in arr:
        c = target - i
        if c in num:
            pair = (i,c)
            pairs.append(pair)
            
        if i in num:
            num[i] += 1
        else:
            num[i] = 1
    return pairs
arr = [1, 5, 7, -1]
target = 6

print(findPair(arr,target))


#count pairs
# def count_pairs_with_sum(arr, target):
#     num = {}  
#     count = 0   
    
#     for i in arr:
#         c = target - i
#         if c in num:
            
#             count += num[c]
        
       
#         if i in num:
#             num[i] += 1
#         else:
#             num[i] = 1
    
#     return count

# arr = [1, 5, 7, -1]
# target = 6  


# print(count_pairs_with_sum(arr, target))



# #solve question without extra space 

# def find_pair_with_sum(arr, target_sum):
#     # Sort the array
#     arr.sort()

#     # Initialize two pointers at both ends of the array
#     left, right = 0, len(arr) - 1

#     while left < right:
#         current_sum = arr[left] + arr[right]

#         if current_sum == target_sum:
#             # Pair found
#             return arr[left], arr[right]
#         elif current_sum < target_sum:
#             # Move left pointer to increase the sum
#             left += 1
#         else:
#             # Move right pointer to decrease the sum
#             right -= 1

#     # Pair not found
#     return None

# # Example usage:
# arr = [2, 7, 11, 15]
# target = 9
# result = find_pair_with_sum(arr, target)

# if result:
#     print(f"Pair with sum {target}: {result}")
# else:
#     print("No pair found")
