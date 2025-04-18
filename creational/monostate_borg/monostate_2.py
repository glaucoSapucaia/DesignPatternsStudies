# mixin for __str__ and __repr__ methods


class StringReprMixin:
    def __str__(self) -> str:
        params = ", ".join([f"{k} = {v}" for k, v in self.__dict__.items()])
        return f"{self.__class__.__name__}({params})"

    def __repr__(self) -> str:
        return self.__str__()


class MonostateSimple(StringReprMixin):
    # set the attrs from class
    _state = {}

    def __init__(self, nome=None, sobrenome=None):
        self.__dict__ = self._state

        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


if __name__ == "__main__":
    ms1 = MonostateSimple(nome="Glauco")
    ms2 = MonostateSimple(sobrenome="Sapucaia")

    # both instances have the same attrs

    print(ms1)
    print(ms2)
