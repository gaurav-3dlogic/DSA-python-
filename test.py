


def reverseDict(input_dict):
    reversed_dict = {}
    for key,values in input_dict.items():
        reversed_dict[values] = key

    return reversed_dict


input_dict = {"a":1, "b":2, "c":3}
a = reverseDict(input_dict)

print(a)