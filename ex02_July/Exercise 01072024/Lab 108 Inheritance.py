# Inheritance
# Acquiring the properties, Attributes and Behaviour
# Data members and methods

# A concept in OOP that allow a child class to inheritance methods from paren class

# Types of Inheritance :-
# Single = Mostly 80% of time used in API automation
# Multiple
# Multi Level
# Hybrid
# Hierarchical

# ***** Single Inheritance ****
class GrandFather:  # Parent class / Base Call
    key = "abc@123"

    def grandfather_method(self):
        return "Grnadfather Method"


class Father(GrandFather):  # Child Class , Sub class
    def Parent_method(self):
        return "Parent Method"


Parent = Father()
print(Parent.Parent_method())
print(Parent.grandfather_method())  # How Father class able to call GrandFather method- By Single Inheritance
print(Parent.key)
