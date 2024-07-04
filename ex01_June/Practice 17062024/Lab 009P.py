# *args

def print_arguments(*args):  # * args means contains no of arguments
    for i in args:
        print(i, end="\n")


print_arguments("Tanuja", "SHital", "Kunal")  #* args similar to list

# Lets check list example

list_a = ["Apple", "Ball", "Cat", "Dog"]
for i in list_a:
    print(i)

