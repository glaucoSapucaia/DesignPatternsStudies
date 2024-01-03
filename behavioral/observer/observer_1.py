from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict


class IObservable(ABC):
    '''Observable Interface'''

    @property
    @abstractmethod
    def state(self) -> Dict: pass

    @abstractmethod
    def addObserver(self, observer: IObserver) -> None: pass

    @abstractmethod
    def removeObserver(self, observer: IObserver) -> None: pass

    @abstractmethod
    def notifyObservers(self) -> None: pass


class WeatherStation(IObservable):
    '''Concrete Observable'''

    def __init__(self) -> None:
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state: Dict = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notifyObservers()

    def resetState(self) -> None:
        self._state = {}
        self.notifyObservers()

    def addObserver(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def removeObserver(self, observer: IObserver) -> None:
        if observer not in self._observers:
            return
        self._observers.remove(observer)

    def notifyObservers(self) -> None:
        for observer in self._observers:
            observer.update()

        print()


class IObserver(ABC):
    '''Observer Interface'''

    @abstractmethod
    def update(self) -> None: pass


class SmartPhone(IObserver):
    '''Concrete Observer'''

    def __init__(self, name: str, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(
            f'{self.name} | O objeto {observable_name} '
            f'acaba de ser atualizado -> '
            f'{self.observable.state}'
        )


class NoteBook(IObserver):
    '''Concrete Observer'''

    def __init__(self, name: str, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    # alternative method

    def show(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(
            f'{self.name} | O objeto {observable_name} '
            f'acaba de ser atualizado -> '
            f'{self.observable.state}'
        )

    def update(self) -> None:
        self.show()


if __name__ == '__main__':
    # observer tests

    weather_station = WeatherStation()
    smartphone_1 = SmartPhone('Samsung', weather_station)
    smartphone_2 = SmartPhone('Motorola', weather_station)
    smartphone_3 = SmartPhone('IPhone', weather_station)

    notebook_1 = NoteBook('Sony', weather_station)

    # set observers states
    weather_station.addObserver(smartphone_1)
    weather_station.addObserver(smartphone_2)
    weather_station.addObserver(smartphone_3)

    weather_station.state = {'temperature': '34C°'}
    weather_station.state = {'temperature': '30C°'}
    weather_station.state = {'wind_speed': '40km/h'}
    weather_station.state = {'air_humidity': '45%'}

    weather_station.removeObserver(smartphone_1)
    weather_station.resetState()

    weather_station.addObserver(notebook_1)
    weather_station.state = {'climate': 'heavy_rain'}
