
d = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
 
myKeys = list(d.keys())
myKeys.sort()
sorted_dict = {i: d[i] for i in myKeys}
 
print(sorted_dict)