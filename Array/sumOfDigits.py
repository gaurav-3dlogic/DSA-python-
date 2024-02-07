a = 12345


a_str = str(a)

sum_digit = 0


for i in a_str:
    sum_digit += int(i) 
print(sum_digit)