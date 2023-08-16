def rearrangeArray(nums):
    pos_nums = [num for num in nums if num > 0]
    neg_nums = [num for num in nums if num < 0]
    
    result = []
    while pos_nums and neg_nums:
        result.append(pos_nums.pop(0))
        result.append(neg_nums.pop(0))
    
    return result

nums = [3, 1, -2, -5, 2, -4]
result = rearrangeArray(nums)
print(result)
