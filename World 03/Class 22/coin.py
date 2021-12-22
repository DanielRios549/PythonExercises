def format(number: float):
    return f'R${number:.2f}'.replace('.', ',')


def summary(number: float, increase: int = 10, decrease: int = 10):
    print(f'The half of \033[34m{format(number)}\033[m is \033[32m{half(number, True)}\033[m')
    print(f'The double of \033[34m{format(number)}\033[m is \033[32m{double(number, True)}\033[m')
    print(f'Increasing \033[34m{increase}%\033[m, the new price is \033[32m{increment(number, increase, True)}\033[m')
    print(f'Decreasing \033[34m{decrease}%\033[m, the new price is \033[32m{decrement(number, decrease, True)}\033[m')


def increment(number: float, percent: int, coin: bool = False):
    result = number + (number * percent / 100)

    return format(result) if coin is True else result


def decrement(number: float, percent: int, coin: bool = False):
    result = number - (number * percent / 100)

    return format(result) if coin is True else result


def double(number: float, coin: bool = False):
    result = number * 2

    return format(result) if coin is True else result


def half(number: float, coin: bool = False):
    result = number / 2

    return format(result) if coin is True else result
