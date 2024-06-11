#Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
import math

# Calculate Square of given number
print("**Method 1- Calculate Square of number** :")
num1 = input("Enter number the: ")
square = math.pow(2,2)
print("Square of num1 is: ", square)
print(type(square))

print("**Method 2- Calculate Square of number** :")
num1 = float(input("Enter the number: "))
#result = math.pow(float(num1),2)
result = math.pow(num1,2)
print("Square of given number is : ", result)
print(type(square))

# Calculate cube of given number
print("**Calculate Cube of number**")
num2 = float(input("Enter the number : "))
#Cube = math.pow(num2,3)
Cube = (num2) ** 3
print("Cube of given number is : ", Cube)


#Create a program that takes two numbers as input and prints whether the first number is greater than, less than,
#or equal to the second number.

numa1 = float(input("Enter the number a1: "))
numa2 = float(input("Enter the number a2: "))

print("Number a1 is greater than Number a2" if numa1 > numa2 else "Number a1 is less than Number a2" if numa1 < numa2 else "Number a1 is equal to Number a2" )