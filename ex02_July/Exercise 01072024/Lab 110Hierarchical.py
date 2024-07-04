# Hierarchical Inheritance

# 1 Father= Multiple children

class Father:
    def BHK1(self):
        print("1BHK")


class Pramod(Father):
    def BHK2(self):
        print("2BHK")


class Amit(Father):
    def BHK3(self):
        print("3BHK")


class Lucky(Father):

    def No_House(self):
        print("No House")


pramod = Pramod()
pramod.BHK2()
pramod.BHK1()

amit = Amit()
amit.BHK1()
amit.BHK3()
# amit.BHK2 # Not accessible as belongs to pramod

lucky = Lucky()
lucky.No_House()
lucky.BHK1()
