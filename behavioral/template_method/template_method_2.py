from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Pizza(ABC):
    '''Abstract Class'''

    def prepare(self) -> None:
        '''Template Method'''

        self.hookBeforeIngredients()  # hookMethod
        self.addIngredients()  # Abstract
        self.hookAfterIngredients()  # hookMethod
        self.cook()  # Abstract
        self.cut()  # Concrete
        self.serve()  # Concrete

    def cut(self) -> None:
        print(f'Cutting the pizza 😋 | {self.__class__.__name__}')

    def serve(self) -> None:
        print(f'Serving the pizza 😁 | {self.__class__.__name__}')

    # hook methods

    def hookBeforeIngredients(self) -> None: pass

    def hookAfterIngredients(self) -> None: pass

    @abstractmethod
    def addIngredients(self) -> None: pass

    @abstractmethod
    def cook(self) -> None: pass


class PizzaCalabbria(Pizza):
    '''Concrete Class'''

    def addIngredients(self) -> None:
        print('Ingredients => letuce, pepperoni, tomato')

    def cook(self) -> None:
        print('Time => 30min')


class PizzaChicken(Pizza):
    '''Concrete Class'''

    def hookBeforeIngredients(self) -> None:
        print('Washing the chicken')

    def hookAfterIngredients(self) -> None:
        print('Seasoning the chicken')

    def addIngredients(self) -> None:
        print('Ingredients => chicken, cheese, oregano')

    def cook(self) -> None:
        print('Time => 45min')


if __name__ == '__main__':
    # instances
    pizza_calabbria = PizzaCalabbria()
    pizza_chicken = PizzaChicken()

    # executions
    pizza_calabbria.prepare()
    print('-' * 100)
    pizza_chicken.prepare()
