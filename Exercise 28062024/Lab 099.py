class person:
    # Class variables / Instance variables

    name = "Amit"
    age = None

    def walk(self):
        age = 10  # Local Variablee
        print("I am a method")
        print("Hi", self.age)
        print("This is age", age)


# Object_referance = object-> ClassName()
amit = person()
# ObjectReferance.function
amit.walk()
