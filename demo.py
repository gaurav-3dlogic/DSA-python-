#Find duplicate in array

def find_duplicates(arr):
    seen = set()
    dupliate = []

    for i in arr:
        if i in seen:
            dupliate.append(i)
        seen.add(i)
    return dupliate

arr = [1,2,3,4,5,6,7,8,9,10,1,2]

print(find_duplicates(arr))




