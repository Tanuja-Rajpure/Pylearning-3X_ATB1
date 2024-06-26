# Sum of digit


def sum_of_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits = sum_digits + n % 10
        n = n // 10  # Quotient
        # /  - div
        # // Quotient
        # % - Reminder
    return sum_digits


print(sum_of_digits(12345))

#***********************************

def sum_of_digit(n):
    # Base Case
    if n < 10:
        return n
    # Recursive Case
    else:
        return n % 10 + sum_of_digit(n // 10)
print(sum_of_digit(12345))