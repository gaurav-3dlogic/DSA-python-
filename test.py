def getUnion(a, n, b, m):

	# Defining set container s
	s = set()

	# Inserting array elements in s
	for i in range(n):
		s.add(a[i])

	for i in range(m):
		s.add(b[i])
	print("Number of elements after union operation: ", len(s), "")
	print("The union set of both arrays is :" + "")

	print(s, end="") # s will contain only distinct
	# elements from array a and b


# Driver Code
if __name__ == '__main__':
	a = [1, 2, 5, 6, 2, 3, 5, 7, 3]
	b = [2, 4, 5, 6, 8, 9, 4, 6, 5, 4]

	getUnion(a, 9, b, 10)

# This code is contributed by gauravrajput1
