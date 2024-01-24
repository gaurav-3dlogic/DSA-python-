#possible substring

string = "U87TRW1L"

char = []
nums = []

for i in string:
    if i.isalpha():
        char.append(i)
    else:
        nums.append(i)
res = sorted(char) + sorted(nums)
print(','.join(res))
