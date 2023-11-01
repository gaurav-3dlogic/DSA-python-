def reversString(b):
    str = list(b)
    n = len(str)
    s = 0
    e = n - 1


    while s < e:
        str[s] , str[e] = str[e] , str[s]
        s += 1
        e -= 1
        rev = ''.join(str)
        return rev

str = "abc"
reversed_str = reversString(str)
print(reversed_str)


