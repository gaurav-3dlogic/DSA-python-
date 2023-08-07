def selectionSort(arr,n):
    n = len(arr)
    for i in range(n):
        minIndex = i
        
        for j in range(i+1,n):
            
            if arr[j] < arr[minIndex]:
                minIndex = j
                
        arr[minIndex], arr[i] = arr[i] ,arr[minIndex]
    return arr

arr = [1,2,0,-2,9,8]
n = len(arr)
print(selectionSort(arr,n))
        