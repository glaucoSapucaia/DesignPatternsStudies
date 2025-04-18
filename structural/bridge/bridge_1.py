from __future__ import annotations
from abc import ABC, abstractmethod


class IRemoteControl(ABC):
    """Interface Abstraction"""

    @abstractmethod
    def increaseVolume(self) -> None:
        pass

    @abstractmethod
    def decreaseVolume(self) -> None:
        pass

    @abstractmethod
    def power(self) -> None:
        pass


class RemoteControl(IRemoteControl):
    """Interface Abstraction"""

    def __init__(self, device: IDevice) -> None:
        self._device = device

    def increaseVolume(self) -> None:
        self._device.volume += 10

    def decreaseVolume(self) -> None:
        self._device.volume -= 10

    def power(self) -> None:
        self._device.power = not self._device.power


class IDevice(ABC):
    """Implementor Interface"""

    @property
    @abstractmethod
    def volume(self) -> int:
        pass

    @volume.setter
    @abstractmethod
    def volume(self, volume: int) -> None:
        pass

    @property
    @abstractmethod
    def power(self) -> bool:
        pass

    @power.setter
    @abstractmethod
    def power(self, state: bool) -> None:
        pass


class TvSystem(IDevice):
    """Concrete Implementor"""

    def __init__(self) -> None:
        self._volume = 10
        self._state = False
        self._name = self.__class__.__name__

    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, volume: int) -> None:
        if not self._state:
            print("Please, turn TV on!")
            return

        if volume > 100:
            print("Max Volume!")
            return

        if volume < 0:
            print("Mute volume!")
            return

        self._volume = volume
        print(f"Volume set => {self._volume}")

    @property
    def power(self) -> bool:
        return self._state

    @power.setter
    def power(self, state: bool) -> None:
        self._state = state
        print(f"TV on?! => {self._state}")


if __name__ == "__main__":
    # instances
    tv = TvSystem()
    controler = RemoteControl(tv)

    # executions
    controler.increaseVolume()
    controler.power()
    controler.increaseVolume()
    controler.increaseVolume()
    controler.increaseVolume()
    controler.increaseVolume()
    controler.increaseVolume()
    controler.increaseVolume()
    controler.increaseVolume()
    controler.increaseVolume()
    controler.increaseVolume()
    controler.increaseVolume()
    controler.increaseVolume()

    controler.decreaseVolume()
    controler.decreaseVolume()
    controler.decreaseVolume()
    controler.decreaseVolume()
    controler.decreaseVolume()
    controler.decreaseVolume()
    controler.decreaseVolume()
    controler.decreaseVolume()
    controler.decreaseVolume()
    controler.decreaseVolume()
    controler.decreaseVolume()

    controler.increaseVolume()
    controler.increaseVolume()
    controler.increaseVolume()

    controler.power()
    controler.increaseVolume()
