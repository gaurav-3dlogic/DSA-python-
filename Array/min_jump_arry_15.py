def jump(nums):
    ans = 0
    end = 0
    far = 0

    for i in range(len(nums) - 1):
      far = max(far, i + nums[i]) 
      if far >= len(nums) - 1:
        ans += 1
        break
      if i == end:      # Visited all the items on the current level
        ans += 1        # Increment the level
        end = far  # Make the queue size for the next level

    return ans


nums = [2,3,1,1,4]
print(jump(nums))