a = "Hey gaurav how are you gaurav ok gaurav"
r = "gaurav"

# Initialize position and count variables
pos = []
count = 0

# Loop through the string to find all occurrences of the substring
for i in range(len(a)):
    if a[i:i+len(r)] == r:
        pos.append(i)
        count += 1

# Print the results
print("The substring '{}' occurs {} times in the string.".format(r, count))
print("The substring '{}' occurs at positions: {}".format(r, pos))


# Time complexity of this program is O(n) and space complexity is O(n)