string = input("Please enter string: ")

res = []

for i in range(len(string)):
    for j in range(i+ 1,len(string)):
        res.append(string[i:j])

print(','.join(res))