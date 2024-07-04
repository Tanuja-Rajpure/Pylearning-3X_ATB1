my_dict = {
    'b': 2,
    'a': 3,
    'c': 4
}

# To find a key

for k, v in my_dict.items():
    print("Key value from my dict are :", k, ":", v)
    if k == 'c':
        print("Key value for is c is found")

op = 'c' in my_dict
print("Key value for b is found: ", op)

# FILTERS in Python:
# The Filter() function is built in function in Python
# Allows to filter elements in list , tuple, set
# Filter basically work with function which give tru or false
# We can apply filter to each element of a list, if it is true, it will return num, if not then won't return.
# Filter always work with function
# First argument of filter is filter only

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(num):
    return num % 2 == 0


new_list_even = filter(is_even, numbers)
print("EVen num list is: ", list(new_list_even))
