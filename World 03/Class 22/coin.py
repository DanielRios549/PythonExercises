def format(number: float):
    return f'R${number:.2f}'.replace('.', ',')


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
