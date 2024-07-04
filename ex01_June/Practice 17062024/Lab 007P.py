
# TYpe- No return type with default arguments

def say_hello_arg_default(name = "Pramod"):
    print("Hello", name)

say_hello_arg_default()            # we are calling fun and taking default value
say_hello_arg_default("Deeksha")
say_hello_arg_default(name= "Sachin")

# Type return tpe with arguments

def sum_number_arguments_return(a , b):
    return a + b

result = (sum_number_arguments_return(3 , 4))
result1 = (sum_number_arguments_return(a = 50 ,  b = 4))
result2 = (sum_number_arguments_return(b = 150 ,  a = 5))
print(result)
print(result1)
print(result2)