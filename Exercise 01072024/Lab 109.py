class Parent:
    gold = "2KG"

    def BHK2(self):
        print("2BHK")


class Child(Parent):
    def BHK3(self):
        print("3BHK")


child_object = Child()
child_object.BHK3()
child_object.BHK2()
child_object.gold
print(child_object.gold)

father_obj = Parent()
father_obj.gold
father_obj.BHK2()
