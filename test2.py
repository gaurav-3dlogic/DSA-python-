d = {
    'ravi': 10,"sorca":8,"sherca":90,"jeo":80
}

myKeys = list(d.keys())
myKeys.sort()
sorted_dict = {i: d[i] for i in myKeys}


print(sorted_dict)