# a = {"Gaurav":100,"saini":200,"python":500,"java":100}
# del a["java"]
# print(a)


#Another example
test_dict = {"banana":10,"Mango":20,"chinese":12,"spanish":100}
res = {key: val for key, val in test_dict.items() if key != "banana"}
print(res)

