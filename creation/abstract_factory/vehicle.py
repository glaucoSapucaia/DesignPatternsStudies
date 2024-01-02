from abc import ABC, abstractmethod


class VehicleLux(ABC):
    @abstractmethod
    def goToTheCustomer(self) -> None: pass


class VehiclePop(ABC):
    @abstractmethod
    def goToTheCustomer(self) -> None: pass


# North Zone classes


class VehicleLuxNZ(VehicleLux):
    def goToTheCustomer(self) -> None:
        print('Looking for the customer | CarLux | North Zone')


class VehiclePopNZ(VehiclePop):
    def goToTheCustomer(self) -> None:
        print('Looking for the customer | CarPop | North Zone')


class MotorcycleNZ(VehiclePop):
    def goToTheCustomer(self) -> None:
        print('looking for the customer | Motorcycle | North Zone')

# South Zone classes


class VehicleLuxSZ(VehicleLux):
    def goToTheCustomer(self) -> None:
        print('Looking for the customer | CarLux | South Zone')


class VehiclePopSZ(VehiclePop):
    def goToTheCustomer(self) -> None:
        print('Looking for the customer | CarPop | South Zone')


class MotorcycleSZ(VehiclePop):
    def goToTheCustomer(self) -> None:
        print('looking for the customer | Motorcycle | South Zone')

# Abstract factory


class VehicleFactory(ABC):

    @staticmethod
    @abstractmethod
    def getVehicleLux() -> VehicleLux: pass

    @staticmethod
    @abstractmethod
    def getVehiclePop() -> VehiclePop: pass

    @staticmethod
    @abstractmethod
    def getMotorcycle() -> VehiclePop: pass

# Region factories


class NorthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def getVehicleLux() -> VehicleLux:
        return VehicleLuxNZ()

    @staticmethod
    def getVehiclePop() -> VehiclePop:
        return VehiclePopNZ()

    @staticmethod
    def getMotorcycle() -> VehiclePop:
        return MotorcycleNZ()


class SouthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def getVehicleLux() -> VehicleLux:
        return VehicleLuxSZ()

    @staticmethod
    def getVehiclePop() -> VehiclePop:
        return VehiclePopSZ()

    @staticmethod
    def getMotorcycle() -> VehiclePop:
        return MotorcycleSZ()


class CLient:
    def searchCustomer(self):
        for factory in [NorthZoneVehicleFactory(), SouthZoneVehicleFactory()]:
            vehicle_lux = factory.getVehicleLux()
            vehicle_lux.goToTheCustomer()

            vehicle_pop = factory.getVehiclePop()
            vehicle_pop.goToTheCustomer()

            motorcycle = factory.getMotorcycle()
            motorcycle.goToTheCustomer()


if __name__ == '__main__':
    client = CLient()
    client.searchCustomer()
