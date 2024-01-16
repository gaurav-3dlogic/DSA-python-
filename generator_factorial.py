f = int(input("Enter a number: "))


def gen(f):
    for i in range(1,f+1):
        fact = 1
        
        for j in range(1,i+1):
            fact = fact * j
        yield fact
    
for fact in gen(f):
    print(fact)

