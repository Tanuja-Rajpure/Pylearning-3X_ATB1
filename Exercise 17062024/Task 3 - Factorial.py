n = 5
result = 5 * 4 * 3 * 2 * 1

n = 4
result = 4 * 3 * 2 * 1

n = 4

n = int(input("Enter value of n = "))
factorial = 1
# result = math.factorial(5)
# print(result)

for i in range(1, n + 1):  # n+1 used as in range we always take range till n-1, so to get range till n, we need to give n+1
    factorial = factorial * i

print("Factorial is:", factorial)


