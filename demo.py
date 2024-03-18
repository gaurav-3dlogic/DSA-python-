n = int(input("Enter a number: "))

if n > 1:
    is_prime = True  # Assume n is prime initially

    for i in range(2, n):
        if n % i == 0:
            is_prime = False  # If n is divisible by any number in the range, it's not prime
            break

    if is_prime:
        print("Number is prime")
    else:
        print("Number is not prime")
else:
    print("Number is not prime")
