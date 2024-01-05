'''Use flyweight only all conditions below are TRUE

1. The application has a large number of objects.
2. Objects in large quantities and high creation costs.
3. Part of the object can become extrinsic.
4. Many objects can be replaced by few shared objects.
5. The application does not depend on the indentity ogf the objects.
'''

from __future__ import annotations
from typing import List, Dict


class Client:
    '''Context Class'''

    def __init__(self, name: str) -> None:
        # intrinsic attrs
        self.name = name
        self._addresses: List = []

        # extrinsic attrs
        self.address_number: str
        self.address_details: str

    def addAddress(self, address: Address) -> None:
        self._addresses.append(address)

    def listAddresses(self) -> None:
        for address in self._addresses:
            address.showAddress(self.address_number, self.address_details)


class Address:
    '''Flyweight Object'''

    def __init__(self, street: str, neighborhood: str, zip_code: str) -> None:
        self._street = street
        self._neighborhood = neighborhood
        self._zip_code = zip_code

    def showAddress(self, address_number: str, address_detail: str) -> None:
        print(
            self._street, address_number, self._neighborhood, address_detail,
            self._zip_code
        )


class AddressFactory:
    '''Flyweight factory'''

    # flyweight pool
    _addresses: Dict = {}

    def _getKey(self, **kwargs) -> str:
        return ''.join(kwargs.values())

    def getFlyweight(self, **kwargs) -> Address:
        '''Create the flyweight keys'''

        key = self._getKey(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('Object already create')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Create new object')

        return address_flyweight


if __name__ == '__main__':
    # instances
    address_factory = AddressFactory()

    # addresses factory
    a1 = address_factory.getFlyweight(
        street='Av. 1', neighborhood='Bonfim', zip_code='124536-980'
    )

    a2 = address_factory.getFlyweight(
        street='Av. 1', neighborhood='Bonfim', zip_code='124536-980'
    )

    # clients
    person1 = Client('person1')
    person1.address_number = '49'
    person1.address_details = 'apto 20'
    person1.addAddress(a1)

    person2 = Client('person2')
    person2.address_number = '120'
    person2.address_details = 'house'
    person2.addAddress(a2)

    # executions
    person1.listAddresses()
    print('_' * 100)
    person2.listAddresses()
