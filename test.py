def is_palindrome(s):
    return s == s[::-1]

def all_palindromes(arr):
    for item in arr:
        if not is_palindrome(str(item)):
            return False
    return True

arr = [121, 1331, 1221, 3443]
result = all_palindromes(arr)
print(result)  # Output: True



# is_palindrome = lambda s: s == s[::-1]

# def all_palindromes(arr):
#     return all(map(lambda item: is_palindrome(str(item)), arr))

# arr = [121, 1331, 1221, 3443]
# result = all_palindromes(arr)
# print(result)  # Output: True

