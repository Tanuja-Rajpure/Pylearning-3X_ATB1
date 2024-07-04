class Dog:
    name = None  # Every class should have starting value, so we give none, and further for different object we can give different names
    id = None

    # Constructor?- > Special method
    # Used to initialize value of the instance variable/ attributes
    # Automatically when an object is created from class.
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def sleep(self):
        print("Who is Sleeping-> " + self.name)


dog1 = Dog("Chow", "1")
dog2 = Dog("Mow", "2")

print(f'{dog1.name} has Id {dog1.id}')
print(f'{dog2.name} has Id {dog2.id}')

dog1.sleep()
dog2.sleep()

