# Reverse String 
def reverse_string(arr):
    start , end = 0, len(arr) -1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
arr = [1,2,3]
print(reverse_string(arr))