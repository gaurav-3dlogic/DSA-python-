def jump(a):
    ans = 0
    far = 0
    end = 0
    
    for i in range(len(a) - 1):
        far = max(far, i + a[i])
        if far >= len(a) - 1:
            ans += 1 
            break 
        if i == end:
            ans += 1
            end = far
            
    return ans 


a = [2,3,1,1,4]
print(jump(a))