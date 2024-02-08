def long_word(n,str):
    b = n.split(' ')
    word_len = []
    for i in b:
        if len(i) > n:
            word_len.append(i)
    return word_len

print(long_word(4,"Hey there my name is veeroal"))
