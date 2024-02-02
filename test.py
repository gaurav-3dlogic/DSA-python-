# Number is binary or not

num = input("Enter a number: ")

# check each digit of the number 
for i in range(len(num)): 
	
	# check if digit is 0 or 1 
	if num[i] not in "01": 
		
		# print result 
		print("No, the number is not binary")
		break
		
else: 
	print("Yes, the number is binary")