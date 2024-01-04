from collections.abc import Iterator, Iterable
from typing import List, Any


class MyIterator(Iterator):
    '''Iterator Class'''

    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = 0

    def __next__(self) -> Any:
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration


class MyReverseIterator(Iterator):
    '''Iterator Class'''

    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = -1

    def __next__(self) -> Any:
        try:
            item = self._collection[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration


class MyCollection(Iterable):
    '''Aggregate Class'''

    def __init__(self) -> None:
        self._items: List[Any] = []
        # self._my_iterator = MyIterator(self._items)  # Iterator that runs out

    def __iter__(self) -> Iterator:
        # return self._my_iterator  # Iterator taht runs out
        return MyIterator(self._items)

    def reverseIterator(self) -> Iterator:
        return MyReverseIterator(self._items)

    def addItem(self, value: Any) -> None:
        self._items.append(value)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._items})'


if __name__ == '__main__':
    # instances
    my_collection = MyCollection()

    # executions
    print(my_collection)
    my_collection.addItem(1)
    my_collection.addItem(2)
    my_collection.addItem(3)
    my_collection.addItem(4)
    my_collection.addItem(5)

    print(my_collection)

    for i in my_collection:
        print(i)
    print('_' * 100)
    for i in my_collection.reverseIterator():
        print(i)
