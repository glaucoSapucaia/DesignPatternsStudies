"""The state pattern exclude several conditionals operations | if ..."""

from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    """Context Class"""

    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        self.state.pending()

    def approve(self) -> None:
        self.state.approve()

    def reject(self) -> None:
        self.state.reject()


class OrderState(ABC):
    """State Abstract Class"""

    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None:
        pass

    @abstractmethod
    def approve(self) -> None:
        pass

    @abstractmethod
    def reject(self) -> None:
        pass


class PaymentPending(OrderState):
    """Concrete State Class"""

    def pending(self) -> None:
        print("The order is ALREADY in PENDING status")

    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print("State CHANGE | APPROVED")

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print("State CHANGE | REJECTED")


class PaymentApproved(OrderState):
    """Concrete State Class"""

    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print("State CHANGE | PENDING")

    def approve(self) -> None:
        print("The order is ALREADY in APPROVED status")

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print("State CHANGE | REJECTED")


class PaymentRejected(OrderState):
    """Concrete State Class"""

    def pending(self) -> None:
        print("Impossible to change status to PENDING | REJECTED")

    def approve(self) -> None:
        print("Impossible to change status to APPROVED | REJECTED")

    def reject(self) -> None:
        print("The order is ALREADY in REJECTED status")


if __name__ == "__main__":
    # instances
    order1 = Order()
    order2 = Order()

    # executions
    order1.pending()
    order1.approve()
    order1.pending()
    order1.reject()
    order1.approve()
    order1.pending()
    order1.reject()

    order2.pending()
    order2.approve()
