a = [12, 10, 23, -9, 2, 1]

# Find the range of elements in the list a
max_val = max(a)
min_val = min(a)
range_val = max_val - min_val + 1

# Create a count array to store the frequency of elements
count = [0] * range_val

# Count the frequency of each element in the list
for num in a:
    count[num - min_val] += 1

# Reconstruct the sorted list using the count array
sorted_list = []
for i in range(range_val):
    sorted_list.extend([i + min_val] * count[i])

print(sorted_list)
