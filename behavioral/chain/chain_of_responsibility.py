from __future__ import annotations
from abc import ABC, abstractmethod


class Handler(ABC):
    '''Abstract Handler'''

    def __init__(self) -> None:
        self.sucessor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str: pass


class HandlerABC(Handler):
    '''Concrete Handler'''

    def __init__(self, sucessor: Handler) -> None:
        self.sucessor = sucessor
        self.letters = ['A', 'B', 'C']

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'{self.__class__.__name__} | {letter}'
        return self.sucessor.handle(letter)


class HandlerDEF(Handler):
    '''Concrete Handler'''

    def __init__(self, sucessor: Handler) -> None:
        self.sucessor = sucessor
        self.letters = ['D', 'E', 'F']

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'{self.__class__.__name__} | {letter}'
        return self.sucessor.handle(letter)


class HandlerGHI(Handler):
    '''Concrete Handler'''

    def __init__(self) -> None:
        self.letters = ['G', 'H', 'I']

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'{self.__class__.__name__} | {letter}'
        return f'{self.__class__.__name__} | REQUEST FAILURE'


if __name__ == '__main__':
    # instances
    handler_ghi = HandlerGHI()
    handler_def = HandlerDEF(handler_ghi)
    handler_abc = HandlerABC(handler_def)

    # executions
    print(handler_abc.handle('A'))
    print(handler_abc.handle('D'))
    print(handler_abc.handle('H'))
    print(handler_abc.handle('W'))
