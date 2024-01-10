#Moves zero in Right side
# logic apne non zero ko left side m shift krlo
def moveZero(nums):

    nonZero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[nonZero] , nums[i] = nums[i], nums[nonZero]
            nonZero += 1

nums = [1,0,0,2,13]
moveZero(nums)
print(nums)

# Time Complexity: O(n)
# Space Complexity: O(1)
