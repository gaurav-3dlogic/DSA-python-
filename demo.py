def MinMin(dict):
    maxVal = float("-Inf")
    minVal = float("Inf")

    for k, v in dict.items():
        if v > maxVal:
            maxVal = v
        if v < minVal:
            minVal = v
    return maxVal, minVal

dict = {"a":1,"b" : 2,"c":3 }

print(MinMin(dict))