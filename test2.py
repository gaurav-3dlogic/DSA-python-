a = 1678


x = a

res = 0


while(a > 0):
    res = res * 10 + a % 10
    a = a // 10

if(x == res):
    print("Palindrome")
else:
    print("Not Palindrome")