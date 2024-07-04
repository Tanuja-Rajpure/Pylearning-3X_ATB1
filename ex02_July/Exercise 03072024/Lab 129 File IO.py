
# File IO


try:
    with open('example.txt', 'r') as file:
        print(file.read())


except FileNotFoundError as fnfe:
    print("I am unable to find file, please check file name")

finally:
    print("Closing the file")
    try:
        file.close()  # Close has to be executed , even we find file or not
    except NameError as ne:
        print(ne)
