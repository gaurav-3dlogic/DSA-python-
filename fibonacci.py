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

# def fibonacci(n):
#     # Initialize the first two Fibonacci numbers
#     a, b = 0, 1
#     # Generate Fibonacci numbers up to n
#     while a <= n:
#         yield a
#         a, b = b, a + b

# # Generate the Fibonacci series up to 100
# for num in fibonacci(40):
#     print(num)


#Third Apporach 


n = int(input("Enter a number: "))

a = 0
b = 1
z = 0

while(n >= z):
    print(z)
    z = a + b
    a = b
    b = z

