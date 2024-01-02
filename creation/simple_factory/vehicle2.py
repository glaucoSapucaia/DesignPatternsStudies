# Returns an instance of the factory to the client

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def goToTheCustomer(self) -> None: pass


class CarLux(Vehicle):
    def goToTheCustomer(self) -> None:
        print('Looking for the customer | CarLux')


class CarPop(Vehicle):
    def goToTheCustomer(self) -> None:
        print('Looking for the customer | CarPop')


class Motorcycle(Vehicle):
    def goToTheCustomer(self) -> None:
        print('looking for the customer | Motorcycle')


class VehicleFactory:
    def __init__(self, type_vehicle: str) -> None:
        self.vehicle = self.getVehicle(type_vehicle)

    @staticmethod
    def getVehicle(type_vehicle: str) -> Vehicle:
        if type_vehicle == 'lux':
            return CarLux()
        if type_vehicle == 'pop':
            return CarPop()
        if type_vehicle == 'motorcycle':
            return Motorcycle()
        assert 0, "Unknown vehicle"

    def goToTheCustomer(self):
        self.vehicle.goToTheCustomer()


if __name__ == '__main__':
    from random import choice
    available_cars = ['lux', 'pop', 'motorcycle']

    for i in range(10):
        car = VehicleFactory(choice(available_cars))
        car.goToTheCustomer()
