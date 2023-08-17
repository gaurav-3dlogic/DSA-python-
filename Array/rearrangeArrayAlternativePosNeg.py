def rearrangeArray(nums):
        pos_nums = []
        neg_nums = []
        
        for num in nums:
            if num > 0:
                pos_nums.append(num)
            elif num < 0:
                neg_nums.append(num)
        
        result = []
        i = 0
        while pos_nums and neg_nums:
            if i % 2 == 0:
                result.append(pos_nums.pop(0))
            else:
                result.append(neg_nums.pop(0))
            i += 1
        
        # Add the remaining elements from pos_nums or neg_nums
        result.extend(pos_nums)
        result.extend(neg_nums)
        
        return result

nums = [3, 1, -2, -5, 2, -4]
result = rearrangeArray(nums)
print(result)
