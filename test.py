#string = "A12B7EBOM"
string = "A12B7EBOM"
char = []
nums = []

for i in string:
    if i.isalpha():
        char.append(i)
    else:
        nums.append(i)
res = sorted(char)+sorted(nums)

print(','.join(res))
