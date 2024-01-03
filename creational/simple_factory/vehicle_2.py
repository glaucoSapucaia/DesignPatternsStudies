# Returns the instantiated object to the customer

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
    @staticmethod
    def getVehicle(type_vehicle: str) -> Vehicle | None:
        if type_vehicle == 'lux':
            return CarLux()
        if type_vehicle == 'pop':
            return CarPop()
        if type_vehicle == 'motorcycle':
            return Motorcycle()
        assert 0, "Unknown vehicle"


if __name__ == '__main__':
    from random import choice
    available_cars = ['lux', 'pop', 'motorcycle']

    for i in range(10):
        car = VehicleFactory.getVehicle(choice(available_cars))
        car.goToTheCustomer()  # type: ignore
