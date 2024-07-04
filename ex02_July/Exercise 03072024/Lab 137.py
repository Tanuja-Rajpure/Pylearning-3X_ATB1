try:
    with open("text1.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as fnfe:
    print(fnfe)
finally:
    file.close()
