def Revrsedict(dict):
    maxValue = float("-Inf")
    minValue = float("Inf")
    for key, val in dict.items():
        if val < maxValue:
            maxValue = val
        elif val > minValue:
            minValue = val
        
    return maxValue, minValue
dict = {"a":1, "b":2, "c":3, "d":4}

print(Revrsedict(dict))        

