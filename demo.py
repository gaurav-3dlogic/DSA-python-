a = 132

x = a

res = 0

while a > 0:
    res = res * 10 + a % 10
    a = a // 10

if res == x:
    print("Number is palindrome")
else:
    print("Number is not palindrome")