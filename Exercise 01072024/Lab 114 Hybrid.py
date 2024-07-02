# Hybrid

# Multiple type of inheritance
# Such as Single, multilevel,  hierarical

class A():
    def methodA(self):
        return "Method A"


class B(A):
    def methodB(self):
        return "Method B"


class C(A):
    def methodC(self):
        return "Method C"


class D(C, B):
    def methodD(self):
        return "Method D"


d = D()
print(d.methodD())
print(d.methodC())
print(d.methodA())
print(d.methodB())


def multiple_return_one():
    return 99, "Tanuja", True


print("It will return", multiple_return_one())
