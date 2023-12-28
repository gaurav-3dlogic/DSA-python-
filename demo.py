def find_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)

    # If no duplicates are found
    return None

# Example usage:
arr = [1, 3, 4, 2, 2]
duplicate = find_duplicate(arr)
print("Duplicate:", duplicate)
