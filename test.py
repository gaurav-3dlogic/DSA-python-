def find_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)


    return None

arr = [1,2,3,4,5,1]
duplicate = find_duplicate(arr)
print(duplicate)