string = input("Enter a string: ")
result = []


for i in range(len(string)):
    for j in range(i + 1, len(string) +1 ):
        result.append(string[i:j])

print(','.join(result))