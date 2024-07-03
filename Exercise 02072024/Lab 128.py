# try, except, finally

try:
    num1 = int(input("Enter a num1: "))
    num2 = int(input("Enter a num2: "))
    result = num1/num2
except ValueError as ve:
    print(Ve)
except ZeroDivisionError as zde:
    print(zde)
else:
    print(f'')
finally:
    print("I will be executed any how")