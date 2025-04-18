"""Proxy Pattern

Proxy Virtual => Controls access to CREATION and USAGE RESOURCES.

Proxy Remote => Controls access to REMOTE SERVERS RESOURCES.

Proxy Protection => Controls access to AUTHENTICATION and PERMISSION RESOURCES.

Proxy Intelligent => Controls access to REAL OBJECT and PERFORM TASKS.

A Proxy can perform many tasks like:
-> Create log
-> Authenticate user
-> Distribute services
-> Create cache
-> Create and destroy objects
-> Postpone executions
-> etc
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict, Any
from time import sleep


class IUser(ABC):
    """User Subject Interface"""

    firstname: str
    lastname: str

    @abstractmethod
    def getAddresses(self) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def getAllUserData(self) -> Dict[str, Any]:
        pass


class User(IUser):
    """Concrete Subject User"""

    def __init__(self, firstname: str, lastname: str) -> None:
        """Use sleep to simulate REQUEST"""

        sleep(2)
        self.firstname = firstname
        self.lastname = lastname

    def getAddresses(self) -> List[Dict[str, Any]]:
        """Use sleep to simulate REQUEST"""

        sleep(2)
        return [{"street": "A", "number": 120}]

    def getAllUserData(self) -> Dict[str, Any]:
        """Use sleep to simulate REQUEST"""

        sleep(2)
        return {"cpf": "111.111.111.11", "id": "A5342677"}


class UserProxy(IUser):
    """Proxy Class"""

    def __init__(self, firstname: str, lastname: str) -> None:
        """Lazy Instantiation | _real_user, _user_addresses and _all_user_data

        CACHE simulation
        """

        self.firstname = firstname
        self.lastname = lastname

        # lazy instantiation
        self._real_user: User
        self._user_addresses: List[Dict[str, Any]]
        self._all_user_data: Dict[str, Any]

    def getRealUser(self) -> None:
        """Checks the value of the _real_user attr before instantiating it"""

        if not hasattr(self, "_real_user"):
            self._real_user = User(self.firstname, self.lastname)

    def getAddresses(self) -> List[Dict[str, Any]]:
        """Checks the value of the _user_addresses attr before instantiating it"""

        self.getRealUser()

        if not hasattr(self, "_user_addresses"):
            self._user_addresses = self._real_user.getAddresses()

        return self._user_addresses

    def getAllUserData(self) -> Dict[str, Any]:
        """Checks the value of the _all_user_data attr before instantiating it"""

        self.getRealUser()

        if not hasattr(self, "_all_user_data"):
            self._all_user_data = self._real_user.getAllUserData()

        return self._all_user_data


if __name__ == "__main__":
    # instances
    person1 = UserProxy("fernando", "pessoa")

    # executions
    print(person1.firstname)
    print(person1.lastname)

    # lazy response
    print(person1.getAddresses())
    print(person1.getAllUserData())

    # Instant response | CACHE attrs from PROXY CLASS
    for i in range(20):
        print(person1.getAddresses())
