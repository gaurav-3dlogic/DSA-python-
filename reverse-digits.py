n = int(input("Enter a number: "))

reverse = 0


while(n > 0):
    reverse = reverse * 10 + n % 10
    n //= 10
print("The reverse number is",reverse)

