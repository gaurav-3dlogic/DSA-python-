
def reverseString(str):
    b = list(str)
    s = 0
    e = len(b) - 1


    while(s < e):
        b[s] , b[e] = b[e], b[s]
        s += 1
        e -= 1

       
    return ''.join(b) 

str = "abc"
print(reverseString(str))

