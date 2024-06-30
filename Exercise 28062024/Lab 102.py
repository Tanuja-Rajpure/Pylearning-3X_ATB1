
# Encapsulation ?
# Wrapping / hiding of the data / data binding ?
# Protect the data
# Reviling functionlity and hiding the data

# Encapsulation- Bind the data variables with methods
# Data Member -/ Class variables
# Methods- Function within the class
# Wrapping . binding data variables with methods
# Hide the data members / class / instance variable by only uing methods

class car:
    name = None
    password = "123"

    def __init__(self):
        print("I am called when object is created")

    def change_password(self):
        self.password = "9876"

# This is end of the class
XUV = car()
XUV.password = "897359"