class MyClass:

    def __init__(self):
        self.name = "Amit"
        self._email = "privateemailvar@gmail.com"

    def public_func(self):
        print("Public Func")

    def __private_func(self):
        print("This func is private, accessible via another method only")

    def public_func_private(self):
        self.__private_func()
        print(self._email)

# Security- Not everyone can access your method / variables

a = MyClass()
a.public_func()
a.public_func_private()
