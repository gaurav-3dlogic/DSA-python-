def long_word(n,s):
    b = s.split(' ')
    long_word = []
    for i in b:
        if len(i) > n:
            long_word.append(i)
    return long_word
print(long_word(3,"hey there you are where"))


