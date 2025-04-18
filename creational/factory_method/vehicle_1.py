from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def goToTheCustomer(self) -> None:
        pass


class CarLux(Vehicle):
    def goToTheCustomer(self) -> None:
        print("Looking for the customer | CarLux")


class CarPop(Vehicle):
    def goToTheCustomer(self) -> None:
        print("Looking for the customer | CarPop")


class Motorcycle(Vehicle):
    def goToTheCustomer(self) -> None:
        print("looking for the customer | Motorcycle")


class VehicleFactory(ABC):
    def __init__(self, type_vehicle: str) -> None:
        self.vehicle = self.getVehicle(type_vehicle)

    @staticmethod
    @abstractmethod
    def getVehicle(type_vehicle: str) -> Vehicle:
        pass

    def goToTheCustomer(self):
        self.vehicle.goToTheCustomer()


class NorthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def getVehicle(type_vehicle: str) -> Vehicle | None:
        if type_vehicle == "lux":
            return CarLux()
        if type_vehicle == "pop":
            return CarPop()
        if type_vehicle == "motorcycle":
            return Motorcycle()
        assert 0, "Unknown vehicle"


class SouthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def getVehicle(type_vehicle: str) -> Vehicle | None:
        if type_vehicle == "lux":
            return CarLux()
        if type_vehicle == "pop":
            return CarPop()
        assert 0, "Unknown vehicle"


if __name__ == "__main__":
    from random import choice

    north_zone_available_vehicles = ["lux", "pop", "motorcycle"]
    south_zone_available_vehicles = [
        "lux",
        "pop",
    ]

    print("North Zone")
    for i in range(10):
        # north zone
        north_vehicle = NorthZoneVehicleFactory(choice(north_zone_available_vehicles))
        north_vehicle.goToTheCustomer()

    print("_" * 120)

    print("South Zone")
    for i in range(10):
        # south zone
        south_vehicle = SouthZoneVehicleFactory(choice(south_zone_available_vehicles))
        south_vehicle.goToTheCustomer()
