# a = [1,2,3,4,5]


# print([a[-1]] + a[0:-1]) 
#Time complexity = 0(n)
#Space complexity = 0(n)


#second Approach

def cyclically_rotate_array(arr):
    n = len(arr)

    # Store the last element to be moved to the front
    last_element = arr[-1]

    # Shift elements to the right
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    # Move the last element to the front
    arr[0] = last_element

# Example usage:
arr = [1, 2, 3, 4, 5]
cyclically_rotate_array(arr)
print(arr)  # Output: [5, 1, 2, 3, 4]


#Time complexity = 0(n)
#Space complexity = 0(1)


