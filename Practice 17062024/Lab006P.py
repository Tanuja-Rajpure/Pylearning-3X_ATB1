
# Functions-
# Block of code - which can be executed or reused

# Type- Built in functions- Created by python contributors builtins.py - file in python set up
# Used defined function and types
# They can return something
# They cann't return something
# They have parameters or arguments
# They don't have parameters

def say_hello():    # No return type , no parameters / arguments
    print("Hello")

say_hello()

def say_hello():    # No return type , no parameters / arguments
    print("Hello")

result = say_hello()
print(result)   # Its returning none, so no return type

# TYPE 2 - No return type with Parameters or arguments

def say_hello_arg(name):
    print("Hello", name)

say_hello_arg("Tanuja")
say_hello_arg("Manisha")

# Type - Default argument




def say_hello_arg(name):
    print("Hello", name)

result= say_hello_arg("Tanuja")
print(result)                       # Return none ,so no return type