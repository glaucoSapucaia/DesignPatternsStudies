'''Monostate | Design Patterns

'''


class StringReprMixin:
    '''String and Repr

    Set __str__ and __repr__ methods
    '''

    def __str__(self) -> str:
        params = ', '.join([
            f'{k} = {v}' for k, v in self.__dict__.items()
        ])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class Monostate(StringReprMixin):
    ''' Monostate example

    Set the same attrs for diferent instances
    '''

    _state = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, nome=None, sobrenome=None):
        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


if __name__ == '__main__':
    ms1 = Monostate(nome='Glauco')
    ms2 = Monostate(sobrenome='Sapucaia')

    print(ms1)
    print(ms2)
