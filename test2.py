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
# dic = {"a":1,"b":2,"c":3,"d":4}
# rev_dict = {}
# while dic:
#     key,value = dic.popitem()
#     rev_dict[key] = value

# print(str(rev_dict))
    

# revert key with value
# def reverse_dict(input_dict):
#     reversed_dict = {}  # Initialize an empty dictionary to store reversed key-value pairs

#     for key, value in input_dict.items():
#         reversed_dict[value] = key  # Swap key and value in the reversed dictionary

#     return reversed_dict

# # Example usage:
# input_dict = {"a": 1, "b": 2, "c": 3}
# reversed_dict = reverse_dict(input_dict)
# print(reversed_dict)

#Reverse key with values
def reverse_dict(a):
    rev_dict = {}
    for key,value in a.items():
        rev_dict[value] = key
    return rev_dict

a = {"a":1, "b":2, "c":3, "d":4}
print(reverse_dict(a))
