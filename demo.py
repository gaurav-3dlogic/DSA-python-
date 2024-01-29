a = "Hey Gaurav what your problemtic"

b = a.split()

longest_str = ""


for i in b:
    if len(i) > len(longest_str):
        longest_str = i

print(longest_str)

#Time complexity : 0(n)
#Space complexity : 0(1)