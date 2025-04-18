from abc import ABC, abstractmethod
from email.headerregistry import Address


class StringReprMixin:
    def __str__(self) -> str:
        params = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"{self.__class__.__name__}({params})"

    def __repr__(self) -> str:
        return self.__str__()


# product (UML)


class User(StringReprMixin):
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone_numbers = []
        self.addresses = []


# abstract builder (UML)


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self):
        pass

    @abstractmethod
    def addFirstname(self, firstname):
        pass

    @abstractmethod
    def addLastname(self, lastname):
        pass

    @abstractmethod
    def addAge(self, age):
        pass

    @abstractmethod
    def addPhone(self, phone):
        pass

    @abstractmethod
    def addAddress(self, address):
        pass


# concrete builder (UML)


class UserBuilder(IUserBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data

    # return self allows chaining methods

    def addFirstname(self, firstname):
        self._result.firstname = firstname
        return self

    def addLastname(self, lastname):
        self._result.lastname = lastname
        return self

    def addAge(self, age):
        self._result.age = age
        return self

    def addPhone(self, phone):
        self._result.phone_numbers.append(phone)
        return self

    def addAddress(self, address):
        self._result.addresses.append(address)
        return self


# director (UML)


class UserDirector:
    def __init__(self, builder: UserBuilder):
        self._builder = builder

    # chaining methods example

    def withAge(self, firstname, lastname, age):
        self._builder.addFirstname(firstname).addLastname(lastname).addAge(age)

        # create and reset values

        return self._builder.result

    def withAddress(self, firstname, lastname, address):
        self._builder.addFirstname(firstname).addLastname(lastname).addAddress(address)

        # create and reset values

        return self._builder.result


if __name__ == "__main__":
    user_builder = UserBuilder()
    director = UserDirector(user_builder)

    user1 = director.withAge(firstname="João", lastname="Silva", age=27)
    user2 = director.withAddress(
        firstname="Carlos", lastname="Miranda", address="Av. Jacuí, 210 - Centro"
    )

    print(user1)
    print(user2)
    print(id(user1) == id(user2))
