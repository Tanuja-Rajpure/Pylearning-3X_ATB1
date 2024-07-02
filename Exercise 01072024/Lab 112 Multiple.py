# Multiple

class Father:
    def f_money(self):
        return "5"

    def home(self):
        return "This is from Father"


class Mother:
    def m_money(self):
        return "2"

    def home(self):
        return "This is from Mother"


class Son(Mother, Father):
    pass

    #def home(self):
     #   return "This is of Son's Home"


son = Son()
son.f_money()
son.m_money()
son.home()
print(son.home())  # home fun called form Sun class, as Local as a preferance

# This is well known problem in Java- Diamond Problem
# Which is solved by Python Multiple Inheritance

print(son.home()) # As now Son don;t hav home, it will take from other class, which is first preferance, here mother
# It i called Method Resolution Order (MRO)
