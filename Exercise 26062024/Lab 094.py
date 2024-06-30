class Dog:
    name = None  # Every class should have starting value, so we give none, and further for different object we can give different names
    id = None


    # Constructor?
    # Used to initialize value of the instance variable/ attributes
    def sleep(self):
        print("Sleeping")

dog1 = Dog()
print(dog1.name)
dog1.name = "Chow"
print(dog1.name)
dog1.sleep()
print("-------- --------------------")

dog2 = Dog()
print(dog2.name)
dog2.name= "Maw"
print(dog2.name)
# Classes- Is a user defined data type which defines its properties and methods
# Objects is run- time entity. It is a instace of the class. An object can represent a person , olace or any other item