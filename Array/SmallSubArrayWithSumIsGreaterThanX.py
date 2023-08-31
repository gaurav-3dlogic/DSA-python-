'''Input:
A[] = {1, 4, 45, 6, 0, 19}
x  =  51
Output: 3
'''


def sb(a, x, n):  # Corrected parameter order
     
    left = 0
    current = 0
    length = float("inf")
    for i in range(len(a)):
        current += a[i]
        while current > x:  # Changed 'a' to 'x'
            length = min(length, i + 1 - left)
            
            current -= a[left]
            left += 1
    if length == float("inf"):
        return 0
    return length

a = [1, 4, 45, 6, 0, 19]
x = 51
n = len(a)
print(sb(a, x, n))

