n = int(input("Enter the number:  "))

def num(n):
    if n == 0:
        return 0
    num(n -1)
    print(n)
num(n)


