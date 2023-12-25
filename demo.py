#Reverse a list in python
def reverseString(s):
    start , end = 0 , len(s) -1
    while start <= end:
        s[start] , s[end] = s[end] , s[start]
        start += 1
        end -= 1
    return s
s = [1,2,3,4]
print(reverseString(s))

