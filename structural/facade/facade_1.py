'''Using Observer example to façade pattern'''

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List, Dict


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


class WeatherStationFacade:
    '''Façade Class'''

    def __init__(self) -> None:
        # observer tests
        self.weather_station = WeatherStation()
        self.smartphone_1 = SmartPhone('Samsung', self.weather_station)
        self.smartphone_2 = SmartPhone('Motorola', self.weather_station)
        self.smartphone_3 = SmartPhone('IPhone', self.weather_station)
        self.notebook_1 = NoteBook('Sony', self.weather_station)

        # set observers states
        self.weather_station.addObserver(self.smartphone_1)
        self.weather_station.addObserver(self.smartphone_2)
        self.weather_station.addObserver(self.smartphone_3)
        self.weather_station.addObserver(self.notebook_1)

    def addObserverWithFacade(self, observer: IObserver) -> None:
        '''Optional add oberver method'''

        self.weather_station.addObserver(observer)

    def removeObserverWithFacade(self, observer: IObserver) -> None:
        '''Optional remove oberver method'''

        self.weather_station.removeObserver(observer)

    def changeState(self, state: Dict[str, Any]) -> None:
        '''Optional change state method'''

        self.weather_station.state = state

    def removeSmartphone1(self) -> None:
        '''Remove specific Oberver'''

        self.weather_station.removeObserver(self.smartphone_1)

    def removeNotebook1(self) -> None:
        '''Remove specific Oberver'''

        self.weather_station.removeObserver(self.notebook_1)

    def resetStateFacade(self) -> None:
        '''Optional reset state method'''

        self.weather_station.resetState()


if __name__ == '__main__':
    # instances
    weather_station = WeatherStationFacade()

    # executions
    weather_station.removeSmartphone1()
    weather_station.removeNotebook1()
    weather_station.resetStateFacade()

    weather_station.changeState({'temperature': '27C°'})
    weather_station.changeState({'wind_speed': '36km/h'})
    weather_station.changeState({'air_humidity': '40%'})
