from __future__ import annotations
from copy import deepcopy
from typing import Any, Dict, List


class Memento:
    '''Memento Immutable Class'''

    def __init__(self, state: Dict[str, Any]) -> None:
        '''Set attr _state | Python Immutable Class issue'''

        self._state: Dict[str, Any]
        super().__setattr__('_state', state)

    def getState(self) -> Dict[str, Any]:
        return self._state

    def __setattr__(self, __name: str, __value: Any) -> None:
        '''Set this Class immutable'''

        raise AttributeError(f'{self.__class__.__name__} | I am immutable!')


class ImageEditor:
    '''Originator Class'''

    def __init__(self, name: str, width: str, height: str) -> None:
        self.name = name
        self.width = width
        self.height = height

    def saveState(self) -> Memento:
        '''Save Memento original object'''

        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.getState()

    def __str__(self) -> str:
        return f'{self.__class__.__name__} | {self.__dict__}'


class CareTaker:
    '''CareTaker Class

    Similar to Command patterns
    '''

    def __init__(self, originator: ImageEditor) -> None:
        self._originator = originator
        self._mementos: List[Memento] = []

    def backup(self) -> None:
        self._mementos.append(self._originator.saveState())

    def restore(self) -> None:
        if not self._mementos:
            return

        self._originator.restore(self._mementos.pop())


if __name__ == '__main__':
    # instances
    image = ImageEditor('picture_1.jpg', '280px', '280px')
    caretaker = CareTaker(image)

    # tests
    caretaker.backup()
    image.name = 'another_name'
    image.width = '401px'
    image.height = '401px'
    caretaker.backup()

    image.name = 'another_name2'
    image.width = '400px'
    image.height = '400px'
    caretaker.backup()

    image.name = 'another_name3'
    image.width = '402px'
    image.height = '402px'

    caretaker.restore()
    caretaker.restore()
    caretaker.restore()
    caretaker.restore()

    # executions
    print(image)
