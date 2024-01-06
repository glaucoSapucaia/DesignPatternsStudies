'''COMPOSITE

Application only hierarchical structures (trees)
'''

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class IComponent(ABC):
    '''Component Abstract CLass'''

    @abstractmethod
    def printContent(self) -> None: pass

    @abstractmethod
    def getPrice(self) -> float: pass

    def add(self, child: IComponent) -> None: pass

    def remove(self, child: IComponent) -> None: pass


class Component(IComponent):
    '''Composite Class'''

    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[IComponent] = []

    def printContent(self) -> None:
        print(f'\n{self.name}\n')
        for child in self._children:
            child.printContent()

    def getPrice(self) -> float:
        return sum(
            [child.getPrice() for child in self._children]
        )

    def add(self, child: IComponent) -> None:
        self._children.append(child)

    def remove(self, child: IComponent) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(IComponent):
    '''Leaf Class'''

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def printContent(self) -> None:
        print(f'{self.name} -> {self.price}')

    def getPrice(self) -> float:
        return self.price


if __name__ == '__main__':
    # instances
    # leaf
    t_shirt1 = Product('t_shirt1', 29.90)
    t_shirt2 = Product('t_shirt2', 19.90)
    t_shirt3 = Product('t_shirt3', 9.90)

    smartphone1 = Product('smartphone1', 1000.45)
    smartphone2 = Product('smartphone2', 1400.45)

    # composite
    t_shirt_box = Component('t_shirt_box')
    smartphone_box = Component('smartphone_box')
    client_box = Component('client_box')

    # relations
    t_shirt_box.add(t_shirt1)
    t_shirt_box.add(t_shirt2)
    t_shirt_box.add(t_shirt3)

    smartphone_box.add(smartphone1)
    smartphone_box.add(smartphone2)

    client_box.add(t_shirt_box)
    client_box.add(smartphone_box)

    # executions
    t_shirt_box.printContent()
    print('_' * 100)
    smartphone_box.printContent()
    print('_' * 100)
    client_box.printContent()
    print(client_box.getPrice())
