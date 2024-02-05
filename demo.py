num = input("Enter a number: ")


for i in range(len(num)):
    if num[i] not in "01":
        print("Number is not Binary")
        break
else:
    print("Number is Binary")
