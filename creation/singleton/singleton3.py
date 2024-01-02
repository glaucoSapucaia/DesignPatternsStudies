# order of execution of dunder methods

# class Meta(type):
#     def __call__(cls, *args, **kwargs):
#         print('__call__ method METACLASS')
#         return super().__call__(*args, **kwargs)


# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print('__new__ method')
#         return super().__new__(cls)

#     def __init__(self, nome) -> None:
#         print('__init__ method')
#         self.nome = nome

#     def __call__(self, x, y):
#         print('__call__ method', self.nome, x + y)


# if __name__ == '__main__':
#     p1 = Pessoa('Ana')
#     print(p1.nome)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.tema = 'escuro'
        self.font = '40px'


if __name__ == '__main__':
    as1 = AppSettings()
    as2 = AppSettings()
    as3 = AppSettings()

    print(as1.tema)
    as1.tema = 'claro'

    # equal objects have equal attrs

    print(as2.tema)
    print(as3.tema)
    print(as1 == as3)
