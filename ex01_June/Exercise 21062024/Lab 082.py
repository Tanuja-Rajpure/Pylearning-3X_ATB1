my_dict = {'a': 1, 'b': 2, 'c': 4, 'a': 95, 'd': 4}  # Keys must be unique, valiue can be duplicated
print(my_dict)
print(len(my_dict))
print(list(my_dict.keys()))
print(list(my_dict.values()))

for keys, values in my_dict.items():
    print(keys, values)
