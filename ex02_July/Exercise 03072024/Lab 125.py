#try:
    # Try this code , if error
#excet:
    # Give exception

# print("Indentation Error")

#result = 5 + "5" # TypeError: unsupported operand type(s) for +: 'int' and 'str'

#int("Pramod") # ValueError: invalid literal for int() with base 10: 'Pramod'

#print(undefined_variable) #NameError: name 'undefined_variable' is not defined

#my_list = [1, 2, 3]
#print(my_list[3])  # IndexError: list index out of range, as it is start from 0

#my_dict = {'a': 1, 'b' : 2}
#print(my_dict['c'])             # KeyError: 'c'

#result 10/0  # zerodivision error

# import 'non_existace_module'  # No module name 'non estistance error

### ******** Differance in exception and error *******

# Error can not be handled
# Programme recovery is not possible

# Where exceptions(error) can be handled
# Programme recovery is possible
try:
    while True print("Hello")
except Exception as e:
    print(e)
