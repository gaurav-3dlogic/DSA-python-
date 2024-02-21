def max_min_dict(dict1):
    max_val = float("-Inf")
    min_val = float("Inf")
    for key, value in dict1.items():
        if value < max_val:
            max_val = value
        if value > min_val:
            min_val = value
    return max_val, min_val

dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(max_min_dict(dict1))