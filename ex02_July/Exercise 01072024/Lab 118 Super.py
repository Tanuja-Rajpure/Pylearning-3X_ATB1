class Father():
    def home(self):
        print("1BHK")


class Son(Father):
    def home(self):
        super().home()  # Super can only give your Father info , not of Grand father
        print("No House")


pramod = Son()
pramod.home()
