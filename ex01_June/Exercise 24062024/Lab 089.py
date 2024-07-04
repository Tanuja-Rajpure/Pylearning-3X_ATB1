# Recursion
# COncept where function call itseif to solve a problem
# Key conecpts
# 1. Base case
# 2. Recursive case

# Factorial
def factorial(n):
    # Base case
    if n == 0 or n == 1:


return 1
else:
return n * (factorial(n - 1))
