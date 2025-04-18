class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    # problems when using initializer methods with singleton
    def __init__(self) -> None:
        self.tema = "Escuro"
        self.font = "20px"


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = "claro"

    print(as1.tema)

    # as2 is the same object as as1 | the same ID in memory
    as2 = AppSettings()

    # due the __init__ method, the tema attr always overwritten
    print(as1.tema)
