# Programming technique
# Where fun() call itself to solve a problem

# key concepts
# 1. Base case
# 2. Recursive case

# Factorial programme

n = int(input("Enter number to calculate factorial: "))


def factorial(n):
    # Base Case - If n=0 / 1 this is min we can go till max of n
    if n == 0 or n == 1:
        return 1
    # Recursive case - > It will keep running till it reaches to base case
    else:
        return n * factorial(n - 1)


print("Factorial of number is: ", factorial(n))
