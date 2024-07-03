# Method Overloading
# Does not supported in Python ?
# In traditional sense
# It is only supported by only default arguments

# Method Overloading = Two or more methods/ functions with same name but different arguments
class MathUtils(object):
    def add(self, a, b, c=0):
        return a + b + c

    def add(self, a, c):
        return a - c


Math = MathUtils()
op1 = Math.add(3, 4)
op2 = Math.add(1)
op3 = Math.add(1, 2, 3)

print(op1)

# Here output return -1, so as fun name is same add, it is taking onlt latest to retrun result a - c
