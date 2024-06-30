# Hpw tp create a class

class person:
    # Attributes
    name = None
    id = None
    age = None
    phone_number = None

    # Behaviour
    def talk(self):  # No Argument , no return
        print("I can talk")

    def sleep(self, name):  # 1 Argument , No return
        print("I am also method")
        print("Sleep", name)

    def sleep2(self, name):  # 1 Argument , 1 return
        print("I am also method")
        return None

    def walk_return(self):  # No argument, return type
        return "I am walking"

    def walk(self):  # No argument, no return type
        print("I am walking")


# Create object of the person class
#  Objectreferance = Object --> className()
surya = person()
surya.name = "Surya Prakash"
surya.talk()

ritika = person()
ritika.name = "Ritika Gupta"
ritika.walk()
