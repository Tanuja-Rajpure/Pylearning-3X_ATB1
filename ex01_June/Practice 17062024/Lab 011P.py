# LEAP year program

# Year divisible by 4
# Not by the hundread
# Divisible by 400


year = int(input("Enter a year: "))

year % 4 == 0
year % 100 != 0
year % 400 == 0

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not Leap year")
# *********** ANoter method **********8
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is no a leap year.")

