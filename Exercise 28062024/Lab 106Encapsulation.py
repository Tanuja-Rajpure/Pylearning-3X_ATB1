class BankAccount:

    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_func(self):
        print(self.__private_var)

    def depositefunc(self, amount):
        self.balance += amount

    def __withdraw(self, amount):
        self.balance -= amount

    def __show_balance(self):
        print("Your balance is: ", self.balance)

    def if_u_r_authenticated(self, flag):
        if flag:
            self.__show_balance()
        else:
            print("Not Allowed")

    def if_u_r_authenticated_user(self, auth, amount):
        if auth:
            self.__withdraw(amount=amount)
        else:
            print("Not Allowed")


jp_chase = BankAccount()
jp_chase.depositefunc(100)
jp_chase.if_u_r_authenticated(True)
jp_chase.if_u_r_authenticated_user(True, 10)
jp_chase.if_u_r_authenticated(True)

secret_pass = input("Enter PIN to see balance: ")
your_amount = int(input("Enter your amt to withdraw"))

if secret_pass == "12345":
    jp_chase.if_u_r_authenticated_user(True, amount= your_amount)
    jp_chase.if_u_r_authenticated(True)
else:
    jp_chase.if_u_r_authenticated_user(False)
