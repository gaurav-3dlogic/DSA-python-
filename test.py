
#first approch
a = [12, 35, 9, 56, 24]

temp = a[0]
a[0] = a[-1]
a[-1] = temp

print(a)


#second approch
a = [12, 35, 9, 56, 24]

temp = a[0] ,a[-1]

a[-1],a[0] = temp

print(a)


#Third approch

a = [12, 35, 9, 56, 24]
a[0] ,a[-1] = a[-1],a[0]
print(a)




