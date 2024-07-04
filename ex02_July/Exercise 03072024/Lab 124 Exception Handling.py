# How to handle exception
print("----Start of the programme----")
try:
    # code
    a = int(input("Enter no num1:"))
    b = int(input("Enter no num2:"))
    c = a / b
    print("Result div is:", c)

except Exception as e:
    print(e)
    print("Please check you input")

print("----End of the programme----")
