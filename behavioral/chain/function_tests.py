'''Conception tests with functions'''


def handlerABC(letter: str) -> str:
    letters = ['A', 'B', 'C']

    if letter in letters:
        return f'handlerABC => {letter}'
    return handlerDEF(letter)


def handlerDEF(letter: str) -> str:
    letters = ['D', 'E', 'F']

    if letter in letters:
        return f'handlerDEF => {letter}'
    return handlerGHI(letter)


def handlerGHI(letter: str) -> str:
    letters = ['G', 'H', 'I']

    if letter in letters:
        return f'handlerGHI => {letter}'

    return f'Fail | {letter}'


if __name__ == '__main__':
    print(handlerABC('A'))
    print(handlerABC('H'))
    print(handlerABC('W'))
