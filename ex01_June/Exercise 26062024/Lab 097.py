class student:

    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))

    def display(self):
        print(f'Your name is {self.name}, Age is {self.age} years')

#ObjectReferance = CLassName()
student = student()
student.display()