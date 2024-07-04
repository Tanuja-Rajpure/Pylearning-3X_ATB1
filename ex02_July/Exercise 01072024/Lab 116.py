#

class GF:
    def car(self):
        return "Old Car"


class F(GF):
    def car(self):
        return "Honda"


class S(F):
    def car(self):
        return "Lambo"


son = S()
son.car()
print("Preference given to Local i.e Son's Car: ", son.car())
