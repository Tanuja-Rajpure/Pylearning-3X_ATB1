# Lets do this program without recursion

def sum_of_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits = sum_digits + n % 10
        # sum_digits += n % 10 #(Here += is, sum_digits + n%10)
        n = n // 10  # % Remainder, / Division , // quotient
    return sum_digits


print("Print sum of digits 12345 is: ", sum_of_digits(12345))
