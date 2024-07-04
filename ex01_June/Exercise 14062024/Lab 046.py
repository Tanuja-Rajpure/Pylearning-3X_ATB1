
browser = input("Enter a browser\n")
match browser:
    case "chrome":
        print("Chrome code executed")
    case "edge":
        print("edge code executed")
    case "firefox":
        print("firefox code executed")
    case _:
        print("No Idea")