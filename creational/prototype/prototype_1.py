"""Care with copies of objects

immutable data !! are copied !!

    bool
    int
    float
    tuple
    str
    ...

mutable data !! are not copied !!
--- they have the same reference in memory ---

    list
    set
    dict
    class (can be changed)

"""

# use __future__ to fix fake importations errors

from __future__ import annotations


from copy import deepcopy


class StringReprMixin:
    def __str__(self) -> str:
        params = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"{self.__class__.__name__}({params})"

    def __repr__(self) -> str:
        return self.__str__()


class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: list[Address] = []

    def addAddress(self, address: Address) -> None:
        self.addresses.append(address)

    # the prototype method !!!

    def clone(self) -> Person:
        return deepcopy(self)


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == "__main__":
    glauco = Person("glauco", "sapucaia")
    endereco_glauco = Address("rua jacui", "233A")
    glauco.addAddress(endereco_glauco)

    # here, i need to create a deepcopy object
    # mutables data
    # (--- they have the same reference in memory ---)

    esposa_glauco = glauco.clone()
    esposa_glauco.firstname = "Gabriela"

    print(glauco)
    print(esposa_glauco)
