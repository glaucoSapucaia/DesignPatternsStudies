from abc import ABC, abstractmethod


class AbstractClass(ABC):
    """Abstract Class"""

    def templateMethod(self) -> None:
        """Template Method"""

        self.hook()
        self.operation1Method()
        self.anotherBaseMethod()
        self.operation2Method()

    def anotherBaseMethod(self) -> None:
        print("Another Base Method")

    # hook method | For specific circumstances
    def hook(self) -> None:
        pass

    @abstractmethod
    def operation1Method(self) -> None:
        pass

    @abstractmethod
    def operation2Method(self) -> None:
        pass


class ConcreteClass1(AbstractClass):
    """Concrete Class"""

    def operation1Method(self) -> None:
        print(f"Operation 1 ok! - {self.__class__.__name__}")

    def operation2Method(self) -> None:
        print(f"Operation 2 ok! - {self.__class__.__name__}")

    def hook(self) -> None:
        print("Using the hook method")


class ConcreteClass2(AbstractClass):
    """Concrete Class"""

    def operation1Method(self) -> None:
        print(f"Operation 1 ok! - {self.__class__.__name__}")

    def operation2Method(self) -> None:
        print(f"Operation 2 ok! - {self.__class__.__name__}")


if __name__ == "__main__":
    # instances
    c1 = ConcreteClass1()
    c2 = ConcreteClass2()

    # executions
    c1.templateMethod()
    print()
    c2.templateMethod()
