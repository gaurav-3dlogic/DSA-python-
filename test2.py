def jump(nums):
    ans = 0
    end = 0
    far = 0

    for i in range(len(nums)-1):
        far = max(far, i + nums[i])
        if far >= len(nums) -1:
            ans += 1 
            break

        if i == end:
            ans += 1
            end = far
    return ans

nums =   [2,3,1,1,4]
print(jump(nums))

