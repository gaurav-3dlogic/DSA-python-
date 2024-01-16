def print_num(n):
    for i in range(n):
        yield i

for num in print_num(5):
    print(num)



