from __future__ import annotations
from abc import ABC, abstractmethod


class SoundSystem:
    def __init__(self) -> None:
        self.mode: PlayMode = ModeRadio(self)
        self.playing = 0

    def pressNext(self) -> None:
        self.mode.pressNext()

    def pressPrevious(self) -> None:
        self.mode.pressPrevious()

    def changeMode(self) -> None:
        self.playing = 0
        self.mode.changeMode()


class PlayMode(ABC):
    """State Abstract Class"""

    def __init__(self, device: SoundSystem) -> None:
        self.device = device

    @abstractmethod
    def pressNext(self) -> None:
        pass

    @abstractmethod
    def pressPrevious(self) -> None:
        pass

    @abstractmethod
    def changeMode(self) -> None:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}"


class ModeRadio(PlayMode):
    """State Concrete Class"""

    def pressNext(self) -> None:
        self.device.playing += 100
        print(f"ADVANCING to the radio station | {self.device.playing}")

    def pressPrevious(self) -> None:
        self.device.playing -= 100 if self.device.playing > 0 else 0
        print(f"GOING BACK to the radio station | {self.device.playing}")

    def changeMode(self) -> None:
        self.device.mode = ModeMp3(self.device)
        print(f"CHANGE to mode | {self.device.mode}")


class ModeMp3(PlayMode):
    """State Concrete Class"""

    def pressNext(self) -> None:
        self.device.playing += 1
        print(f"ADVANCING to the mp3 file | {self.device.playing}")

    def pressPrevious(self) -> None:
        self.device.playing -= 1 if self.device.playing > 0 else 0
        print(f"GOING BACK to the mp3 file | {self.device.playing}")

    def changeMode(self) -> None:
        self.device.mode = ModeRadio(self.device)
        print(f"CHANGE to mode | {self.device.mode}")


if __name__ == "__main__":
    # instances
    device = SoundSystem()

    # executions
    device.pressNext()
    device.pressPrevious()
    device.pressNext()
    device.pressNext()
    device.changeMode()
    device.pressNext()
    device.pressPrevious()
    device.pressPrevious()
