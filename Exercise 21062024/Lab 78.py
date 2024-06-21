# Decorator

# Whats is decorator-> A function which takes another function as a arguments
# Returns a new fun that usually extends

def my_decorator(func):
    def wrapper():
        print("Starting----")
        print("******")
        func()
        print("*******")
        print("Ending")

    return wrapper()


@my_decorator
def say_hell0():
    print("Say Hello")


#say_hell0()  No ned to call say hello, it is called by decorator
