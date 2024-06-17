# *args - anu number of arguments

def sum3(a, b, c):
    return a + b + c


result = sum3(4, 5, 9)
print(result)


def sum_three(a=2, b=99, c=0):
    return a + b + c


result1 = sum_three()
result2 = sum_three(1, 2)
result3 = sum_three(1, 2, 5)
result4 = sum_three(a=221, b=66, c=5)
