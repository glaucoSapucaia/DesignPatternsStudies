from __future__ import annotations
from copy import deepcopy
from typing import List
from dataclasses import dataclass

# ingredients


@dataclass
class Ingredient:
    """Abstract Ingredient"""

    price: float


@dataclass
class Bread(Ingredient):
    """Concrete Ingredient"""

    price: float = 1.50


@dataclass
class Sausage(Ingredient):
    """Concrete Ingredient"""

    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    """Concrete Ingredient"""

    price: float = 7.99


@dataclass
class Egg(Ingredient):
    """Concrete Ingredient"""

    price: float = 1.50


@dataclass
class PotatoStick(Ingredient):
    """Concrete Ingredient"""

    price: float = 0.99


@dataclass
class MashedPotatoes(Ingredient):
    """Concrete Ingredient"""

    price: float = 2.25


@dataclass
class Cheese(Ingredient):
    """Concrete Ingredient"""

    price: float = 6.35


# components


class Hotdog:
    """Component Class

    "Fake Interface"
    """

    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([ingredient.price for ingredient in self._ingredients]), 2)

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingradients(self) -> List[Ingredient]:
        return self._ingredients

    # __str__ and __repr__ methods

    def __str__(self) -> str:
        return f"{self.name}({self.price} => {self.ingradients})"

    def __repr__(self) -> str:
        return self.__str__()


class SimpleHotdog(Hotdog):
    """Sub Component Class"""

    def __init__(self) -> None:
        self._name: str = self.__class__.__name__
        self._ingredients: List[Ingredient] = [Bread(), Sausage()]


class SpecialHotdog(Hotdog):
    """Sub Component Class"""

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
    """Decorator Class "Fake Interface"

    Use to prevent "CLASS EXPLOSION"
    """

    def __init__(self, hotdog: Hotdog) -> None:
        self.hotdog = hotdog

    @property
    def price(self) -> float:
        return self.hotdog.price

    @property
    def name(self) -> str:
        return self.hotdog.name

    @property
    def ingradients(self) -> List[Ingredient]:
        return self.hotdog.ingradients


class CustomHotdogWithBacon(CustomHotdog):
    """Decorator Concrete Class"""

    def __init__(self, hotdog: Hotdog) -> None:
        super().__init__(hotdog)

        self._ingredient = Bacon()
        self._ingredients = deepcopy(self.hotdog.ingradients)
        self._ingredients.append(self._ingredient)

    @property
    def price(self) -> float:
        return round(sum([ingredient.price for ingredient in self._ingredients]), 2)

    @property
    def name(self) -> str:
        return f"{self.hotdog.name} + {self._ingredient.__class__.__name__}"

    @property
    def ingradients(self) -> List[Ingredient]:
        return self._ingredients


if __name__ == "__main__":
    # instances
    simple_hotdog = SimpleHotdog()
    special_hotdog = SpecialHotdog()
    custom_simple_hotdog = CustomHotdogWithBacon(simple_hotdog)
    custom_simple_hotdog2 = CustomHotdogWithBacon(custom_simple_hotdog)

    # executions
    print(simple_hotdog)
    print("_" * 100)
    print(special_hotdog)
    print("_" * 100)
    print(custom_simple_hotdog)
    print("_" * 100)
    print(custom_simple_hotdog2)
