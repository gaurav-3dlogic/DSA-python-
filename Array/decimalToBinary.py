def convertBinary(n):
    if n > 1:
        convertBinary(n // 2)
        print(n % 2, end = "")

dec = 5

convertBinary(dec)
print()
