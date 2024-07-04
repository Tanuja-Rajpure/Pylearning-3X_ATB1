# used defined function use arguments to transfer information to function

# Pass some information to the f(n)
def greet(name):  # name, parameter or arguments
    print("Hi, How are you", name)


greet("Tanuja")
greet("Anuj")
greet("ABC")


#
def allowed_to_attend_python_class(name, password):
    if name == "Tanuja":
        if password == "Yes":
            print("You are allowed")
        else:
            print("Not allowed")


allowed_to_attend_python_class("Tanuja", "Yes")

#Now use match case

def allowed_to_attend_python_class(name):
    match name:
        case "Tanuja":
            print("Tanuja is allowed")
        case "Advika":
            print("Advika is allowed")
        case "Ana":
            print("Ana is allowed")
        case _:
            print("Not allowed")

allowed_to_attend_python_class("Ana")
