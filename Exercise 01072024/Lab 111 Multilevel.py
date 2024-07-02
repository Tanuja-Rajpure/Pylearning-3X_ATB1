# Multilevel Inheritance

# Grandfather to Parent to Child

class GrandFather:
    key_gold = "123"

    def grand_father_method(self):
        return "GrandFather Method"


class Father(GrandFather):
    def Father_method(self):
        return "Father Method"


class child(Father):
    mac_m3_apple = "MAC"

    def child_method(self):
        return "Child Method"


child = child()
child.Father_method()
child.grand_father_method()
child.key_gold()
child.mac_m3_apple()  # Only child can access own not Father nor GF access it

father = Father()
father.grand_father_method()
father.Father_method()
father.key_gold()

grandfather = GrandFather()
grandfather.grand_father_method()
grandfather.key_gold()
