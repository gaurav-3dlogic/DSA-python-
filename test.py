def jums(nums):
    ans = 0
    end = 0
    fartest = 0
    
    for i in range(len(nums)-1):
        fartest = max(fartest, i + nums[i])
        if fartest >= len(nums) - 1:
            ans += 1
            break 
        if i == end:
            ans += 1
            end = fartest
    return ans
nums = [1,2,3,4,5,6,7,8,9]
print(jums(nums))