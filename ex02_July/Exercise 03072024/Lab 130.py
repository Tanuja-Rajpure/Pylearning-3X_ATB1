class XYZ:
    def f1(self):
        try:
            a = int(input("Enter a number : "))
        except Exception as e:
            print("Error-Enter integer only as value of a")
        else:
            print(f'Entered value is integer', a)
        finally:
            print("I will be any how executed")
xyz = XYZ()
xyz.f1()