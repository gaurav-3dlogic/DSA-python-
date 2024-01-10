# def next_permutation(s):
#     # Step 1: Find the rightmost character that is smaller than the character to its right
#     i = len(s) - 2
#     while i >= 0 and s[i] >= s[i + 1]:
#         i -= 1

#     # If no such character is found, the string is already the last permutation
#     if i == -1:
#         return None

#     # Step 2: Find the smallest character to the right of i that is greater than s[i]
#     j = len(s) - 1
#     while s[j] <= s[i]:
#         j -= 1

#     # Step 3: Swap s[i] and s[j]
#     s_list = list(s)
#     s_list[i], s_list[j] = s_list[j], s_list[i]

#     # Step 4: Reverse the substring to the right of i
#     s_list[i + 1:] = reversed(s_list[i + 1:])

#     return ''.join(s_list)

# # Example usage:
# input_str = "acb"
# next_permuted_str = next_permutation(input_str)

# if next_permuted_str:
#     print("Next lexicographically permutation:", next_permuted_str)
# else:
#     print("No next permutation, it's already the last one.")
