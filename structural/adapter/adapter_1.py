from abc import ABC, abstractmethod


class IControl(ABC):
    '''Control Interface'''

    @abstractmethod
    def top(self) -> None: pass

    @abstractmethod
    def right(self) -> None: pass

    @abstractmethod
    def down(self) -> None: pass

    @abstractmethod
    def left(self) -> None: pass


class Control(IControl):
    '''Concrete Control'''

    def top(self) -> None:
        print('Go top')

    def right(self) -> None:
        print('Go right')

    def down(self) -> None:
        print('Go down')

    def left(self) -> None:
        print('Go left')


class NewControl:
    '''Another Concrete Control with different Methods'''

    def moveTop(self) -> None:
        print('Go top')

    def moveRight(self) -> None:
        print('Go right')

    def moveDown(self) -> None:
        print('Go down')

    def moveLeft(self) -> None:
        print('Go left')


class ControlAdapter:
    '''Adapter Class'''

    def __init__(self, new_control: NewControl) -> None:
        self.new_control = new_control

    def top(self) -> None:
        '''Method Adapter'''

        self.new_control.moveTop()

    def right(self) -> None:
        '''Method Adapter'''

        self.new_control.moveRight()

    def down(self) -> None:
        '''Method Adapter'''

        self.new_control.moveDown()

    def left(self) -> None:
        '''Method Adapter'''

        self.new_control.moveLeft()


class AnotherControlAdapter(Control, NewControl):
    '''Multiple Inheritance approach'''

    def top(self) -> None:
        self.moveTop()

    def right(self) -> None:
        self.moveRight()

    def down(self) -> None:
        self.moveDown()

    def left(self) -> None:
        self.moveLeft()


if __name__ == '__main__':
    # instances
    c1 = Control()
    c2 = NewControl()
    c3 = ControlAdapter(c2)
    c4 = AnotherControlAdapter()

    # executions control
    c1.top()
    c1.right()
    c1.down()
    c1.left()

    print('_' * 100)
    # executions new control with adapter
    c3.top()
    c3.right()
    c3.down()
    c3.left()

    print('_' * 100)
    # multiple inheritance executions
    c4.top()
    c4.right()
    c4.down()
    c4.left()
