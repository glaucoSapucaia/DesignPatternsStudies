def singleton(the_class):
    instances = {}

    def getClass(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]

    return getClass

# O decorador singleton faz com que o __init__ seja chamado apenas uma vez


@singleton
class AppSettings:
    def __init__(self) -> None:
        self.tema = 'Escuro'


@singleton
class Test:
    def __init__(self) -> None:
        self.nome = 'test'


if __name__ == '__main__':
    as1 = AppSettings()
    print(as1.tema)
    as2 = AppSettings()
    as2.tema = 'claro'
    print(as1.tema)

    t1 = Test()
    print(t1.nome)
    t2 = Test()
    t2.nome = 'TEST'
    print(t1.nome)
