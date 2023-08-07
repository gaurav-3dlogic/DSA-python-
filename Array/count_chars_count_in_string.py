#First approch
def countChars(a):
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d
a = "gaurav"


# print(countChars(a))

# def countString(a):
#     c = []
    
#     for i in a:
#         count = 0
#         for j in a:
#             if i == j:
#                 count += 1
        
#         c.append((i,count))
#     return list(set(c)) 
# a = "aurav"
# print(countString(a))




