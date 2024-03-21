n = int(input("Enter a number: "))

if n > 1:
    for i in range(2,n):
        if n % i == 0:
            print("Number is not prime")
            break
    else:
        print("Number is prime")
else:
    print("Number is not prime")

#Using While Loop
if n < 1:
    print("Number is not prime")
else:
    div = 2
    while(n ** 0.5 >= div):
        if n % div == 0:
            print("Number is not prime")
            break
        div += 1
    else:
        print("Number is prime")