from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

class Car(Vehicle):
    INCREASED_FUEL_CONSUMPTION = 0.9

    def drive(self, distance):
        needed_fuel_to_drive = distance * (self.fuel_consumption + self.INCREASED_FUEL_CONSUMPTION)
        if self.fuel_quantity >= needed_fuel_to_drive:
            self.fuel_quantity -= needed_fuel_to_drive

    def refuel(self, fuel):
        self.fuel_quantity += fuel

class Truck(Vehicle):
    INCREASED_FUEL_CONSUMPTION = 1.6

    def drive(self, distance):
        needed_fuel_to_drive = distance * (self.fuel_consumption + self.INCREASED_FUEL_CONSUMPTION)
        if self.fuel_quantity >= needed_fuel_to_drive:
            self.fuel_quantity -= needed_fuel_to_drive

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
