class car:
    name = None
    make = None
    model = None

    def __init__(self, name, make, model):
        self.name = name
        self.make = make
        self.model = model

    def start_engine(self):
        print("Starting a car with name", self.name)
        print("Starting a car with make", self.make)
        print("Starting a car with model", self.model)
        print("__________ ... ____________")


# Object referance = className()
lambo = car("Lamborgini", "V2", "202")
# object_referance.function name
lambo.start_engine()

XUV = car("XUV 700", "V6", "205")
# object_referance.function name
XUV.start_engine()
