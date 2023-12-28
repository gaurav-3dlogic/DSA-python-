def jump(nums):
    ans = 0
    end = 0
    far = 0

    for i in range(len(nums)-1):
        far = max(far,i + nums[i])
        if far >= len(nums) - 1:
            ans += 1
            break
        
        elif i == end:
            ans += 1
            end = far
    return ans

nums = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

print(jump(nums))

