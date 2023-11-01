

def reverseArray(arry,s,e):
    while(s < e):
        arry[s] , arry[e] = arry[e] , arry[s] 
        s += 1
        e -= 1


arry = [1,2,3,4,5]

reverseArray(arry,0,4)

print(arry)