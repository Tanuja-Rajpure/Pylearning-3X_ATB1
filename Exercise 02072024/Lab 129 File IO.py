# File IO

with open('tanuja.py', 'r') as file:
    print(file.read())
    file.close()


import os.path
try:

    file = open('tanuja.py')
        print(file.read())

except FileNotFoundError as file:
    print("File not found, check correct file")

finally:
    print("Finlly must be excuted- Closing file")
    file.close()
