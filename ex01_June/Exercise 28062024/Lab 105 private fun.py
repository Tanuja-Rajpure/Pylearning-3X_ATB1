class VWOLogin:

    def __init__(self, name, email, password):
        self.name = name
        self.__email = email
        self.__password = password

    def login_confirm(self):
        if self.__email == "abs@gmail.com" and self.__password == "pass123":
            print("Allowed")

        else:
            print("Not allowed")
    # This is end of the class


page1 = VWOLogin("Tanuja", "abs@gmail.com", "pass123")
# page1._email == not accessible
# page1.__password == not accessible outside the class
page1.login_confirm()
page1.name
print(page1.name)
