a = 121

x = a

res = 0

for i in range(a  ):
    res = res * 10+ a % 10 
    a = a // 2
if(x == res):
    print("Number is palindrom")
else:
    print(" number is not palindrom")