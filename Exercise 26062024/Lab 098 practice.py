class Bank_Account:

    def __init__(self, name, acc_type, amount):
        self.name = name
        self.acc_type = acc_type
        self.amount = amount

    def account_holder(self):
        print(f'Hi {self.name}, your account type is {self.acc_type} and your account balance is {self.amount}')

member = Bank_Account("Tanuja", "Saving", "10,00,000")
member.account_holder()
