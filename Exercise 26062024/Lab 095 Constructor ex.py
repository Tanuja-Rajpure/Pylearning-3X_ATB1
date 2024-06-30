class calc:

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


object_ref = calc()
output = object_ref.sum(3, 4)
object_ref.sub(100, 10)
object_ref.mul(900, 4)
object_ref.div(88, 11)

print(output)
