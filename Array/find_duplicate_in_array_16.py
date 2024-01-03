#First Approach
def duplicates(arr, n): 
    r = []
        
    for i in arr:
        if arr.count(i) > 1:
            if i not in r:
                r.append(i)
    
    if not r:
        return -1
    return r

arr = [2, 3, 1, 2, 3, 0, 0,-1,-1,-2,-1,-2,1]
n = len(arr)

print(duplicates(arr, n))



#Second Approach

# def find_duplicate(arr, n):
#     seen = set()
    
#     for i in range(n):
#         if arr[i] in seen:
#             return arr[i]
#         else:
#             seen.add(arr[i])

#     return -1
  
  
# arr = [1,2,2,3,3]
# n = len(arr)
# print(find_duplicate(arr,n))



#Third approach with time and space

def find_duplicate(nums):
    # Phase 1: Detect the intersection point
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    # Phase 2: Find the entrance to the cycle (duplicate)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

# Example usage:
arr = [1, 3, 4, 2, 2]
duplicate = find_duplicate(arr)
print("Duplicate:", duplicate)
