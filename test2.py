#Fibonacci series


# n = int(input("Enter a number: "))

# a = 0
# b = 1
# z = 0

# while(n >= z):
#     print(z)
#     z = a + b
#     a = b
#     b = z


# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)

# print(fibo(10))


def fibonacci(n):
    a = 0
    b = 1
    while n >= a:
        yield a
        a, b = b, a + b


for i in fibonacci(100):
    print(i)


