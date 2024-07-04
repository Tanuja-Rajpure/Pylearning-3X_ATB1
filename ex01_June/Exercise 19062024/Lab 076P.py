# Tuple - Collection of List

my_list = [1, 2, 3, 4, 5]
print(id(my_list))
my_list[0] = 21
print(my_list)
print(id(my_list))

# tuple is also a list
# tuples are immutable in nature- cannot change value
my_tuple = (1, 2, 3, 4, 5, 5, 6, 7, 8,8)
#my_tuple[0] = 21 # TypeError: 'tuple' object does not support item assignment
print(my_tuple)