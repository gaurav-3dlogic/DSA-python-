# 0 1 1 2 3 5 8 13 21 34

#Fisrt Approach
# n = int(input("Enter a number: "))


# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n -1) + fibo(n -2) 

# print(fibo(n))


#Second Apporach using generator

def fibonacci(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    # Generate Fibonacci numbers up to n
    while a <= n:
        yield a
        a, b = b, a + b

# Generate the Fibonacci series up to 100
for num in fibonacci(10):
    print(num)

