numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def double_me(num):
    return num * 2


new_list_double = map(double_me, numbers)
print("Final doubled list is: ", list(new_list_double))

new_list_double = map(lambda num: num * 2, numbers)
print("Final lambda doubled list is: ", list(new_list_double))

def is_even(num):
    return num % 2 == 0


new_even_list = filter(is_even, numbers)
print("Even num list after filtering", list(new_even_list))

#
