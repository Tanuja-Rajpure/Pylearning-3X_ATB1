# take 2 num from user and add them
# we need to use input function to take input from user

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

result = num1 + num2
#print (result)
#After this it shows concatination of num 1 and num 2- like if n1=1 n2 =2, result=12
# input function take args as string, so we need to convert it into integer
# + -> int sum operation
# + -> str concatination operation

result = int(num1) + int(num2)
print (result)
print (type(result))
