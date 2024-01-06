from __future__ import annotations
from copy import deepcopy
from typing import List
from dataclasses import dataclass

# ingredients


@dataclass
class Ingredient:
    '''Abstract Ingredient'''

    price: float


@dataclass
class Bread(Ingredient):
    '''Concrete Ingredient'''

    price: float = 1.50


@dataclass
class Sausage(Ingredient):
    '''Concrete Ingredient'''

    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    '''Concrete Ingredient'''

    price: float = 7.99


@dataclass
class Egg(Ingredient):
    '''Concrete Ingredient'''

    price: float = 1.50


@dataclass
class PotatoStick(Ingredient):
    '''Concrete Ingredient'''

    price: float = 0.99


@dataclass
class MashedPotatoes(Ingredient):
    '''Concrete Ingredient'''

    price: float = 2.25


@dataclass
class Cheese(Ingredient):
    '''Concrete Ingredient'''

    price: float = 6.35

# components


class Hotdog:
    '''Component Class

    "Fake Interface"
    '''

    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        return round(sum(
            [ingredient.price for ingredient in self._ingredients]
        ), 2)

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingradients(self) -> List[Ingredient]:
        return self._ingredients

    # __str__ and __repr__ methods

    def __str__(self) -> str:
        return f'{self.name}({self.price} => {self.ingradients})'

    def __repr__(self) -> str:
        return self.__str__()


class SimpleHotdog(Hotdog):
    '''Sub Component Class'''

    def __init__(self) -> None:
        self._name: str = self.__class__.__name__
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage()
        ]


class SpecialHotdog(Hotdog):
    '''Sub Component Class'''

    def __init__(self) -> None:
        self._name: str = self.__class__.__name__
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            Cheese(),
            PotatoStick(),
            Bacon(),
            Egg(),
            MashedPotatoes(),
        ]

# decorators


class CustomHotdog(Hotdog):
    '''Decorator Dynamic Class

    Use to prevent "CLASS EXPLOSION"
    '''

    def __init__(self, hotdog: Hotdog, ingredient: Ingredient) -> None:
        self.hotdog = hotdog
        self._ingredient = ingredient
        self._ingredients = deepcopy(self.hotdog.ingradients)
        self._ingredients.append(self._ingredient)

    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self._ingredient.__class__.__name__}'


if __name__ == '__main__':
    # instances
    simple_hotdog = SimpleHotdog()
    egg = Egg()
    mashed_potatoes = MashedPotatoes()
    bacon = Bacon()

    custom_simple_hotdog = CustomHotdog(simple_hotdog, egg)
    custom_simple_hotdog2 = CustomHotdog(custom_simple_hotdog, mashed_potatoes)
    custom_simple_hotdog3 = CustomHotdog(custom_simple_hotdog2, bacon)

    # executions
    print(simple_hotdog)
    print('_' * 100)
    print(custom_simple_hotdog)
    print('_' * 100)
    print(custom_simple_hotdog2)
    print('_' * 100)
    print(custom_simple_hotdog3)
