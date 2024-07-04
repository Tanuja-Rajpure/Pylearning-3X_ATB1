# even odd fun

def find_odd_even_num(num):
    if num % 2 == 0:
        print("Even No")
    else:
        print("Odd No")


find_odd_even_num(66)

# Use Lambda expression

find_odd_even_num = lambda num: num % 2 == 0
print(find_odd_even_num(88))

# ANother method

find_odd_even_num = lambda num: "EVEN Num" if num % 2 == 0 else "ODD num"
print(find_odd_even_num(90))
