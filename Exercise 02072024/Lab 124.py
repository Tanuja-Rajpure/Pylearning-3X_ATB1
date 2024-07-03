# How to handle exception

try:
    # code
    a = int(input("Enter no num1:"))
    b = int(input("Enter no num2:"))
    c = a / b
    print("Result div is:", c)

except Exception as e:
    print("There is an exception Error")

