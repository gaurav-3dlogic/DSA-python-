def least_common_multiple(a,b):
    if a > b:
        greater = a
    elif b > a:
        greater = b
    while(True):
        if ((greater % a == 0)) and (greater % b == 0):
            lcm = greater
            break
        greater = greater + 1
    return lcm

a = 10
b = 20
print(least_common_multiple(a,b))
            
        


