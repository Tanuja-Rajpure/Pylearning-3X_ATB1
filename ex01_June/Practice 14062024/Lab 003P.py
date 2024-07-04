# AND , OR ?

for i in range(1, 10):
    if i % 3 == 0:
        print(i)
    else:
        print(i * 2)


# Multiple conditions
# Switch in Java
# We have Match in Python (We can match number, int, string
# If elif else we can also use

number = int(input("Enter a number \n"))
match number:
    case 1:
        print("Hello this is 1")
    case 3:
        print("Hello this is 3")
    case 40:
        print("Hello this is 40")
    case _:
        print("No Idea")

# USED IN API Automation for selecting browser

browser = str(input("Enter a browser \n"))
browser = browser.lower()
match browser:
    case "chrome":
        print("Use chrome browser")
    case "firefox":
        print("Use firefox browser")
    case "edge":
        print("Use edge browser")
    case _:
        print("Please enter valid browser")