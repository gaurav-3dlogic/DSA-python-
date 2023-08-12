def getPairsCount(arr, n, K):

	count = 0 

	for i in range(0, n):
		for j in range(i + 1, n):
			if arr[i] + arr[j] == K:
				count += 1

	return count


arr = [1, 5, 7, -1]
n = len(arr)
K = 6
print("Count of pairs is",
	getPairsCount(arr, n, K))

