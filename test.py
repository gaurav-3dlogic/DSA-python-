#Reverse a number


a = 12345

res = 0


while a > 0:
    res = res * 10 + a % 10
    a = a // 10

print(res)