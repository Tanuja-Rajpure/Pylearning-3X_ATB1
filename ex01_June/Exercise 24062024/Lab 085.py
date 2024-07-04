## Our focus -> API and Web automation

# Python is very vast lang, not every fun required for API or Web automation

# Filter function - allow to filter the list in a list, tuple , set

my_dict = {
    'a': 2,
    'b': 1,
    'c': 3
}

for k, v in my_dict.items():
    # print(k, ":", v)
    if k == 'b':
        print("key with the name b is found")

OP = 'b' in my_dict
print(OP)

# FILTERS in python -

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Filter on above- even list
new_list_even = [2, 4, 6, 8, 10]


def is_even(num):
    return num % 2 == 0


def is_greater_5(num):
    return num > 5


new_num_even = filter(is_even, numbers)
print("Even num list: ", list(new_num_even))

new_greater_num = filter(is_greater_5, numbers)
print("Num greater than 5 from list:", list(new_greater_num))


def is_odd(num):
    return num % 2 != 0


new_odd_num = filter(is_odd, numbers)
print("Odd num from list", list(new_odd_num))

# We can apply filter to each element of a list, if it true, it will return a num, if false i won't
