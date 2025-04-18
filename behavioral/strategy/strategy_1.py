from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    def __init__(self, total: float, discount: DiscountStrategy) -> None:
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self._total)


# abstract strategy


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float:
        pass


# strategies


class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)


class FiftyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value


# custom seller discount


class CustomDiscount(DiscountStrategy):
    def __init__(self, discount: int) -> None:
        self.discount = discount / 100

    def calculate(self, value: float) -> float:
        return value - (value * self.discount)


if __name__ == "__main__":
    twenty_percent = TwentyPercent()
    fifty_percent = FiftyPercent()
    no_discount = NoDiscount()

    custom_discount_5 = CustomDiscount(5)
    custom_discount_3 = CustomDiscount(3)

    order = Order(1000, twenty_percent)
    order2 = Order(1000, fifty_percent)
    order3 = Order(1000, no_discount)

    order4 = Order(1000, custom_discount_5)
    order5 = Order(1000, custom_discount_3)

    print(order.total, order.total_with_discount)
    print(order2.total, order2.total_with_discount)
    print(order3.total, order3.total_with_discount)
    print(order4.total, order4.total_with_discount)
    print(order5.total, order5.total_with_discount)
