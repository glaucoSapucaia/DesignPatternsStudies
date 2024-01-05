from __future__ import annotations
from abc import ABC, abstractmethod


class IRemoteControl(ABC):
    '''Interface Abstraction'''

    @abstractmethod
    def increaseVolume(self) -> None: pass

    @abstractmethod
    def decreaseVolume(self) -> None: pass

    @abstractmethod
    def power(self) -> None: pass


class RemoteControl(IRemoteControl):
    '''Interface Abstraction'''

    def __init__(self, device: IDevice) -> None:
        self._device = device

    def increaseVolume(self) -> None:
        self._device.volume += 10

    def decreaseVolume(self) -> None:
        self._device.volume -= 10

    def power(self) -> None:
        self.device.power


class IDevice(ABC):
    ''' Implementor Interface'''

    @property
    @abstractmethod
    def volume(self) -> int: pass

    @property
    @abstractmethod
    def power(self) -> bool: pass
