def next_permutation(s):
    i = len(s) - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1
    
    if i == -1:
        return None
    
    j = len(s) - 1
    while s[j] <= s[i]:
        j -= 1

    s_list = list(s)
    s_list[i] , s_list[j] = s_list[j], s_list[i]
    s_list[i + 1:] = reversed(s_list[i + 1:])

    return ''.join(s_list)

input_str = "acb"
next_permutation_str = next_permutation(input_str)


print(next_permutation_str)



