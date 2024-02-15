def wordCOunt(n,str):
    a = str.split(' ')
    res = []
    for i in a:
        if len(i) > n:
            res.append(i)
    return res
print(wordCOunt(3,"Hey Bro what happened"))