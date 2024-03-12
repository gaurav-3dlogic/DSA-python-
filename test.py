a = [1,2,3,4,5,6,7,8,9]
# print([a[-1]] + a[0:-1])

def cyclically_rotate_array(arr):
    n = len(arr)

    last_element = arr[-1]

    for i in range(n - 1, 0,1):
        arr[i] = arr[i - 1]
    arr[0] = last_element

arr = [1,2,3,4,5,6,7,8]
cyclically_rotate_array(arr)
print(arr)  
