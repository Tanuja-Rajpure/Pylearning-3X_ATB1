# Leet Code Programme
# Sum of the digit

number = 12345

sum_of_digit = 15

# Divide no and take its remainder - and each time add remainder
# 12345 / 10 , r = 5
# 1234 / 10 , r = 4
# 123 / 10 , r = 3
# 12 / 10 , r = 2
# 1 / 10, r = 1
# add all r= 15

r1 = number % 10
q1 = number // 10
print("r1:", r1)
print("q1", q1)

r2 = q1 % 10
q2 = q1 // 10
print("r2", r2)
print("q2", q2)

r3 = q2 % 10
q3 = q2 // 10
print("r3", r3)
print("q3", q3)

r4 = q3 % 10
q4 = q3 // 10
print("r4", r4)
print("q4", q4)

r5 = q4 % 10
q5 = q4 // 10
print("r5", r5)
print("q5", q5)

print("Sum of all r is : ", r1 + r2 + r3 + r4 + r5)

# Lets right this in recursive format
# n = 12345
n = int(input("Enter number whose digits sum to be calculated: "))


def sum_of_digits(n):
    # Base Case
    if n < 10:
        return n
    # Recursive case
    else:
        return n % 10 + sum_of_digits(n // 10)


print("Sum of digits is: ", sum_of_digits(n))


# Lets do this program without recursion

def sum_of_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits = sum_digits + n % 10
        #sum_digits += n % 10 #(Here += is, sum_digits + n%10)
        n = n // 10 # % Remainder, / Division , // quotient
    return sum_digits


print("Print sum of digits 12345 is: ", sum_of_digits(12345))
