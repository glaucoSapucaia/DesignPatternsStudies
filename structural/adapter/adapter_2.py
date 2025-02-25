from abc import ABC, abstractmethod


# interface
class IControl(ABC):
    @abstractmethod
    def top(self) -> None: pass

    @abstractmethod
    def right(self) -> None: pass

    @abstractmethod
    def down(self) -> None: pass

    @abstractmethod
    def left(self) -> None: pass


# control
class Control(IControl):
    def top(self) -> None:
        print('Control - top')

    def right(self) -> None:
        print('Control - right')

    def down(self) -> None:
        print('Control - down')

    def left(self) -> None:
        print('Control - left')


# control diferente
class NewControl():
    def newTop(self) -> None:
        print('New Control - top')

    def newRight(self) -> None:
        print('New Control - right')

    def newDown(self) -> None:
        print('New Control - down')

    def newLeft(self) -> None:
        print('New Control - left')


# adapter
class Adapter(IControl):
    def __init__(self, control: NewControl):
        self.control = control

    def top(self) -> None:
        self.control.newTop()
    
    def right(self) -> None:
        self.control.newRight()

    def down(self) -> None:
        self.control.newDown()
    
    def left(self) -> None:
        self.control.newLeft()

if __name__ == '__main__':
    # control
    control = Control()

    control.top()
    control.right()
    control.down()
    control.left()

    print('-' * 100)

    # new control
    new_control = NewControl()

    new_control.newTop()
    new_control.newRight()
    new_control.newDown()
    new_control.newLeft()

    print('-' * 100)

    # adapter
    adapter = Adapter(new_control)

    adapter.top()
    adapter.right()
    adapter.down()
    adapter.left()