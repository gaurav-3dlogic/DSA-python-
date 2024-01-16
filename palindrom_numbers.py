a = 123
res = 0
x = a


while a > 0:
    res = res * 10 + a % 10
    a = a // 10
if x == res:
    print("Number is palindrome")
else:
    print("Number is not palindrome")