# Triangle classifier

a = float(input("Enter a side 1: "))
b = float(input("Enter a side 2: "))
c = float(input("Enter a side 3: "))

if a == b == c:
    print("Triangle is Equilateral")
elif a == b or b == c or c == a:
    print("Triangle is Isosceles")
else:
    print("Triangle is Scelene")