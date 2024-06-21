def my_function():
    a = 10  # Its defined within function , so its a local variable
    print("Hello")
    print(a)

# print(a) --> Not defined in fun , so NameError: name 'a' is not defined

my_function()
