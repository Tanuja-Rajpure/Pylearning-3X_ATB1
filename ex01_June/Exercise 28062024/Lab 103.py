class car:
    name = None

    def __init__(self):
        self.public_var = "public"
        self._protected_var = "Protected"
        self.__private_var = "Private"

    def __private_method(self):
        print("Protected")

    def public_method(self):
        print("I am accessible")

    def printName(self):
        self.__private_method()
        if self.__private_var == "123":
            print("Hi, 123")
            print("Private variable and method can be used by function inside the class")
    # This is end of the CLass


alto = car()
alto.public_var = "Public variable is accessible outside the class"
alto.public_method()
alto.printName()
