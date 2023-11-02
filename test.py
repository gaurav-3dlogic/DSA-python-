a = {"a": 1, "b": 2, "c": 3}
dict_a = {}

# while a:
#     key,values = a.popitem()
#     dict_a[key] = values
# print(str(dict_a))


for key,values in a.items():
    dict_a[values] = key
print(dict_a)

