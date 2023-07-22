def jump(nums):
    ans = 0
    end = 0
    farthest = 0

    for i in range(len(nums) - 1):
      farthest = max(farthest, i + nums[i]) 
      if farthest >= len(nums) - 1:
        ans += 1
        break
      if i == end:      # Visited all the items on the current level
        ans += 1        # Increment the level
        end = farthest  # Make the queue size for the next level

    return ans


nums = [1,0,3,4,5,6,7]
print(jump(nums))