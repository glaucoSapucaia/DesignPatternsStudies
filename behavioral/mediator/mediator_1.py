from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Colleague(ABC):
    """Abstract Colleague"""

    def __init__(self, name: str, mediator: IMediator) -> None:
        self.name = name
        self.mediator = mediator

    @abstractmethod
    def direct(self, msg: str) -> None:
        pass

    @abstractmethod
    def broadcast(self, msg: str) -> None:
        pass

    @abstractmethod
    def sendDirect(self, receiver: Colleague, msg: str) -> None:
        pass


class Person(Colleague):
    """Concrete Colleague"""

    def direct(self, msg: str) -> None:
        print(msg)

    def sendDirect(self, receiver: str, msg: str) -> None:
        self.mediator.direct(self, receiver, msg)

    def broadcast(self, msg: str) -> None:
        self.mediator.broadcast(self, msg)


class IMediator(ABC):
    """Interface Mediator"""

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        pass

    @abstractmethod
    def broadcast(self, colleague: Colleague, msg: str) -> None:
        pass


class ChatRoomMediator(IMediator):
    """Concrete Mediator"""

    def __init__(self) -> None:
        self.colleagues: List[Colleague] = []

    def isColleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues

    def addColleague(self, colleague: Colleague) -> None:
        if self.isColleague(colleague):
            return

        self.colleagues.append(colleague)

    def removeColleague(self, colleague: Colleague) -> None:
        if not self.isColleague(colleague):
            return

        self.colleagues.remove(colleague)

    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        """Direct Concrete Method"""

        if not self.isColleague(sender):
            return

        receiver_obj: List[Colleague] = [
            colleague for colleague in self.colleagues if colleague.name == receiver
        ]

        if not receiver_obj:
            return

        receiver_obj[0].direct(f"{sender.name} to {receiver_obj[0].name} | {msg=}")

    def broadcast(self, colleague: Colleague, msg: str) -> None:
        """Broadcast Concrete Method"""

        if not self.isColleague(colleague):
            return
        print(f"{colleague.name} | {msg=}")


if __name__ == "__main__":
    # instances
    mediator = ChatRoomMediator()
    person1 = Person("Maria", mediator)
    person2 = Person("Luiz", mediator)
    person3 = Person("Fernanda", mediator)
    person4 = Person("Carlos", mediator)

    # add persons
    mediator.addColleague(person1)
    mediator.addColleague(person2)
    mediator.addColleague(person3)
    mediator.addColleague(person4)

    # executions
    person1.broadcast("Alguém por ai?")
    person2.broadcast("To aqui!")

    print("_" * 100)

    mediator.direct(person3, "Luiz", "Blza Luiz?!")
    person4.sendDirect("Maria", "Boa noite!")

    # non-existent person
    person3.sendDirect("Tião", "Bom dia!")
