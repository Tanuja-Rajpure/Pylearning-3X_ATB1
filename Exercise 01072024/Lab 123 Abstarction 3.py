from abc import ABC, abstractmethod


class ATB(ABC):

    @abstractmethod
    def perform_task1(self):
        return "Done1"

    @abstractmethod
    def perform_task2(self):
        return "Done2"


class Amit(ATB):
    def perform_task1(self):
        return "Done1"

    def perform_task2(self):
        return "Done2"


amit = Amit()
print(amit.perform_task1())
print(amit.perform_task2())
