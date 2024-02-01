def find_pair_with_sum(arr, target_sum):
    # Sort the array
    arr.sort()

    # Initialize two pointers at both ends of the array
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target_sum:
            # Pair found
            return arr[left], arr[right]
        elif current_sum < target_sum:
            # Move left pointer to increase the sum
            left += 1
        else:
            # Move right pointer to decrease the sum
            right -= 1

    # Pair not found
    return None

# Example usage:
arr = [2, 7, 11, 15]
target = 9
result = find_pair_with_sum(arr, target)

if result:
    print(f"Pair with sum {target}: {result}")
else:
    print("No pair found")
