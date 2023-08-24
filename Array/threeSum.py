# Input: array = {12, 3, 4, 1, 6, 9}, sumi = 24; 
# Output: 12, 3, 9 

#Brute Force
# def threesumi(arr,sumi):
#     n = len(arr)
#     for i in range(0,n-2):
#         for j in range(i+1,n-1):
#             for k in range(j+1,n):
#                 if arr[i] + arr[j] + arr[k] == sumi:
#                     return arr[i],arr[j],arr[k]


# arr = [1 ,2 ,4 ,3 ,6]
# sumi = 10
# n = len(arr)
# print(threesumi(arr,sumi))

#Optimalsolution 
def find3Numbers(A, n, sum):

	
	A.sort()
	for i in range(0, n-2):
		l = i + 1
		
		r = n-1
		while (l < r):
		
			if( A[i] + A[l] + A[r] == sum):
				print("Triplet is", A[i],
					', ', A[l], ', ', A[r]);
				return True
			
			elif (A[i] + A[l] + A[r] < sum):
				l += 1
			else: # A[i] + A[l] + A[r] > sum
				r -= 1

	return False

A = [1, 4, 45, 6, 10, 8]
sum = 22
n = len(A)

print(find3Numbers(A, n, sum))

