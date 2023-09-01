# Python3 program to implement three way
# partitioning around a given range.

# Partitions arr[0..n-1] around [lowVal..highVal]


def threeWayPartition(arr, n, lowVal, highVal):

	# Initialize ext available positions for
	# smaller (than range) and greater elements
	start = 0
	end = n - 1
	i = 0

	# Traverse elements from left
	while i <= end:

		# If current element is smaller than
		# range, put it on next available smaller
		# position.
		if arr[i] < lowVal:
			arr[i], arr[start] = arr[start], arr[i]
			i += 1
			start += 1

		# If current element is greater than
		# range, put it on next available greater
		# position.
		elif arr[i] > highVal:
			arr[i], arr[end] = arr[end], arr[i]
			end -= 1

		else:
			i += 1

# Driver code
if __name__ == "__main__":
	arr = [1, 14, 5, 4, 2, 54,
		20, 87, 98, 3, 1, 32,10]
	n = len(arr)

	threeWayPartition(arr, n, 10, 20)

	print("Modified array")
	for i in range(n):
		print(arr[i], end = " ")

# This code is contributed by
# sanjeev2552
        