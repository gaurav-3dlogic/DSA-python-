
#First approach
a = {"python":1,"java":2,"js":3}


# del a['js']

# print(a)


#second approach


res = {key:value for key,value in a.items() if key != "python"}

print(res)