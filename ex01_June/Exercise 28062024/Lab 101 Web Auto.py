# Web Automation
# Page - You are going to call
class VWOLoginPage:
    email = None
    password = None

    # This is constructor
    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    # This is function
    def login_confirm(self):
        if self.password == "pass123":
            print("Allowed to login")
        else:
            print("Not Allowed to login")


# This is END of the class

# Below are objects

user_amit = VWOLoginPage("amit123@vwo.com", "pass123")
user_amit.login_confirm()

user_Tanuja = VWOLoginPage("tanuja123@vwo.com", "pass@123")
user_Tanuja.login_confirm()

# Lets try with input
email = input("Enter your email: \n")
password = input("Enter password: \n")
user_Shina = VWOLoginPage(email, password)
user_Shina.login_confirm()
