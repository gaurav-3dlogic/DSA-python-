# reverse array /





def reverseList(a):
    start = 0
    end = len(a) - 1
    while start <= end:
        a[start],a[end] = a[end],a[start]
        start += 1
        end -= 1
    return a
a = [1,2,3,4,5,6,7,8,9]
print(reverseList(a))

