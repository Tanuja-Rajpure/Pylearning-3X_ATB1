# Programming technique
# Where fun() call itself to solve a problem

# key concepts
# 1. Base case
# 2. Recursive case

# Factorial programme

#************** Programme 1 **************
n = int(input("Enter value of n = "))
factorial = 1
# result = math.factorial(5)
# print(result)

for i in range(1, n + 1):  # n+1 used as in range we always take range till n-1, so to get range till n, we need to give n+1
    factorial = factorial * i

print("Factorial is:", factorial)

#*******************************


#************** Programme 2 **************

n = int(input("Enter number to calculate factorial: "))
def factorial(n):
    # Base Case - If n=0 / 1 this is min we can go till max of n
    if n == 0 or n == 1:
        return 1
    # Recursive case - > It will keep running till it reaches to base case
    else:
        return n * factorial(n - 1)


print("Factorial of number is: ", factorial(n))
