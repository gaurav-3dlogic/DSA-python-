#Prime Number

n = int(input("Enter a number: "))

#FOr loop 
# def Prime(n):
#     if n > 1:
#         for i in range(2,n):
#             if n % i == 0:
#                 print("Number is not prime")
#                 break
#         else:
#             print("Number is prime")
#     else:
#         print("Number is not prime")

# Prime(n)

#Using While Loop

if n > 1:
    while(2,n):
        if n % 2 == 0:
            print("Number is not prime")
            break
    else:
        print("Number is prime")
else:
    print("Number is not prime")
        