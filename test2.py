# def max_min(a):
#     max_val = float("-Inf")
#     min_val = float("Inf")
#     for key,values in a.items():
#         if values > max_val:
#             max_val = values
#         if values < min_val:
#             min_val = values

#     return max_val,min_val

# a = {"a":1,"b":2,"c":3,"d":4,"e":5}
# print(max_min(a))


#Reverse dictionary in python 
dic = {"a":1,"b":2,"c":3,"d":4}
rev_dict = {}
while dic:
    key,value = dic.popitem()
    rev_dict[key] = value

print(str(rev_dict))
