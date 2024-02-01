# # Python | Ways to remove a key from dictionary
a = {"Gaurav":100,"saini":200,"python":500,"java":100}
del a['Gaurav']
print(a)



# Another way
test_dict = {"Arushi": 22, "Anuradha": 21,
             "Mani": 21, "Haritha": 21}
new_dict = {key: val for key,
            val in test_dict.items() if key != 'Mani'}
 
# Printing dictionary after removal
print("The dictionary after remove is : " + str(new_dict))

    