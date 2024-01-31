a = "Hey moba are you sure moba love moba"
b = "moba"

pos = []
count = 0


for i in range(len(a)):
    if a[i:i + len(b)] == b:
        pos.append(i)
        count += 1

print("postion",pos)
print("count",count) 