from abc import ABC, abstractmethod


class PyABC(ABC):

    @abstractmethod
    def payfee(self):
        pass

    def enrolled(self):
        print("Enrolled")

class Shubham(PyABC):
   # pass  #   TypeError: Can't instantiate abstract class Shubham without an implementation for abstract method 'payfee

    def payfee(self):
        print('Paid')

shubham = Shubham()
shubham.payfee()
shubham.enrolled()

# Absract method are forceful method, where if the parent class is incomplete(pass) from which child class is inhereting then child class has to complete it


