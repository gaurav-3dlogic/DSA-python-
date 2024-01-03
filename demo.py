def find_duplicates(arr):
    seen = set()
    duplicates = []

    for num in arr:
        if num in seen:
            duplicates.append(num)
        seen.add(num)

    return duplicates

arr = [1, 2, 3, 4, 5, 6, 7, 2, 1]
print(find_duplicates(arr))
