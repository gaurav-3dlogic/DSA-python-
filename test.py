



# def max_min(a):
#     max_val = float("-Inf")
#     min_val = float("-Inf")
#     for key,values in a.items():
#         if values < min_val:
#             min_val = values
#         if values > max_val:
#             max_val = values
#     return max_val, min_val


# a = {"a": 1, "b": 2, "c": 3}
   
# print(max_min(a))


def reverse_dict(a):
    rev_dict = {}
    for key,value in a.items():
        rev_dict[value] = key
    return rev_dict 

a = {"a": 1, "b": 2, "c": 3}
rev_res = reverse_dict(a)
print(rev_res)


