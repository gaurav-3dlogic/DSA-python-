#Find the maximum and minimum element in an array	
arr = [50,10,12,34,21,67]


def findMin(arr):
    m = arr[0]
    n = arr[0]
   
    for i in arr:
        if i < m:
            m = i 
        elif i > m:
            n = i
    print(f"Max num is {n} and min num is {m}")

findMin(arr)            

