def sort012(arr,n):
        l, m, h = 0, 0, len(arr)-1
        
        while m <= h:
            if arr[m] == 0:
                arr[m],arr[l] = arr[l], arr[m]
                l += 1
                m += 1
            
            elif arr[m] == 1:
                m += 1
            
            else:
                arr[m],arr[h] = arr[h], arr[m]
                h -= 1
        
        return arr
        
arr = [0, 1, 2, 0, 1, 2]
        
n = len(arr)
print(sort012(arr,n))