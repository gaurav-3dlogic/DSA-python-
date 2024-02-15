def countN(n,str):

    b = str.split(' ')
    res = []

    for i in b:
        if len(i) > n:
            res.append(i)
    return res

print(countN(2,"Hey fay gayrav u rtar"))