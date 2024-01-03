from abc import ABC, abstractmethod
from typing import Dict, List, Tuple


class Light:
    '''Receiver Class'''

    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'

    def on(self) -> None:
        print(f'{self.name} in {self.room_name} is NOW ON!')

    def off(self) -> None:
        print(f'{self.name} in {self.room_name} is NOW OFF!')

    def changeColor(self, color: str) -> None:
        self.color = color
        print(f'{self.name} in {self.room_name} is NOW with color {self.color}!')


class ICommand(ABC):
    '''Command Interface'''

    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass


class LightOnCommand(ICommand):
    '''Concrete Command'''

    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class ChangeLightColor(ICommand):
    '''Concrete Command'''

    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.light_color_default = self.light.color
        self.color = color

    def execute(self) -> None:
        self.light.changeColor(self.color)

    def undo(self) -> None:
        self.light.changeColor(self.light_color_default)


class RemoteController:
    '''Invoker Class'''

    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}
        self._operations: List[Tuple[str, str]] = []

    def buttonAddCommand(self, btn_id: str, command: ICommand) -> None:
        self._buttons[btn_id] = command

    def buttonExecute(self, btn_id: str) -> None:
        if btn_id not in self._buttons:
            return

        self._buttons[btn_id].execute()
        self._operations.append((btn_id, 'execute'))

    def buttonUndo(self, btn_id: str) -> None:
        if btn_id not in self._buttons:
            return

        self._buttons[btn_id].undo()
        self._operations.append((btn_id, 'undo'))

    def resetOperations(self) -> None:
        if not self._operations:
            print('Empty operations')
            return

        button, action = self._operations[-1]
        if action == 'execute':
            self._buttons[button].undo()
        else:
            self._buttons[button].execute()

        self._operations.pop()


if __name__ == '__main__':
    # receivers instances
    bedroom_light = Light('light', 'bedroom')
    bathroom_light = Light('light', 'bathroom')

    # commands instances
    bedroom_light_on = LightOnCommand(bedroom_light)
    bathroom_light_on = LightOnCommand(bathroom_light)

    bedroom_light_color = ChangeLightColor(bedroom_light, 'green')

    # invoker instances
    remote = RemoteController()
    remote.buttonAddCommand('bedroom_light', bedroom_light_on)
    remote.buttonAddCommand('bathroom_light', bathroom_light_on)
    remote.buttonAddCommand('bedroom_light_color_change', bedroom_light_color)

    # executions
    remote.buttonExecute('bedroom_light')
    remote.buttonExecute('bathroom_light')

    remote.buttonUndo('bedroom_light')

    remote.buttonExecute('bedroom_light_color_change')
    remote.buttonUndo('bedroom_light_color_change')

    # reset (global undo) executions
    print('_' * 100)
    remote.resetOperations()
    remote.resetOperations()
    remote.resetOperations()
    remote.resetOperations()
    remote.resetOperations()
    remote.resetOperations()
