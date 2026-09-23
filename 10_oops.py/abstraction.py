from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract Class
    @abstractmethod
    def start_engine(self):
        pass

class Bike(Vehicle):
    def start_engine(self):
        return "Kick-starting the bike!"

# my_vehicle = Vehicle() # ❌ Error: Cannot instantiate abstract class directly
my_bike = Bike()
print(my_bike.start_engine()) #  Output: Kick-starting the bike!
