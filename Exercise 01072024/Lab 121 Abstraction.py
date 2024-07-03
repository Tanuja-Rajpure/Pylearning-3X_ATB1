 # Abstraction

 # Hiding a details and showing exactly what is required

 # How it differ from Encapsulaion- its within class
 # Absraction withing differnt classes


from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

dog= Dog("Rancho")
dog.sound()
print(dog.sound())

cat = Cat("Cat")
print(cat.sound())

