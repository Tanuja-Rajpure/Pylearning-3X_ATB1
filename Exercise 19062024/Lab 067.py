numbers = [1, 2, 3]


# Collection of iteams

def do_something(my_list):
    my_list.append(45)
    my_list[0] = 9
    return my_list

numbers.append(10)         # Execution will start from calling part
l = do_something(my_list = numbers)
print(l)
