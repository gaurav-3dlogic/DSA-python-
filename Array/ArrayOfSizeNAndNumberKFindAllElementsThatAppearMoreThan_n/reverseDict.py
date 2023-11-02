# # revert key with value
# def reverse_dict(input_dict):
#     reversed_dict = {}  # Initialize an empty dictionary to store reversed key-value pairs

#     for key, value in input_dict.items():
#         reversed_dict[value] = key  # Swap key and value in the reversed dictionary

#     return reversed_dict

# # Example usage:
# input_dict = {"a": 1, "b": 2, "c": 3}
# reversed_dict = reverse_dict(input_dict)
# print(reversed_dict)




#This main Right ans
test_dict = {'gfg': 4, 'is': 2, 'best': 5,'moba': 11}
# printing original dictionary
print("The original dictionary : " + str(test_dict))
reversed_dict = {}
while test_dict:
    key, value = test_dict.popitem()
    reversed_dict[key] = value
 
print("The reversed order dictionary : " + str(reversed_dict))

'''#Explain questions

Certainly! Let me explain the given code step by step:

python
Copy code
test_dict = {'gfg': 4, 'is': 2, 'best': 5}
# printing original dictionary
print("The original dictionary : " + str(test_dict))
reversed_dict = {}
while test_dict:
    key, value = test_dict.popitem()
    reversed_dict[key] = value

print("The reversed order dictionary : " + str(reversed_dict))
Initialization:

test_dict is an original dictionary containing key-value pairs: {'gfg': 4, 'is': 2, 'best': 5}.
Printing the Original Dictionary:

print("The original dictionary : " + str(test_dict)) prints the original dictionary.
Reversing the Dictionary:

An empty dictionary reversed_dict is initialized to store the reversed key-value pairs.

The while loop runs until test_dict is empty.

key, value = test_dict.popitem() pops the last item from test_dict, and its key-value pair is stored in key and value respectively. popitem() removes and returns an arbitrary key-value pair from the dictionary.

reversed_dict[key] = value assigns the popped key-value pair to reversed_dict, effectively reversing the order of key-value pairs.

Printing the Reversed Dictionary:

print("The reversed order dictionary : " + str(reversed_dict)) prints the reversed dictionary.'''
