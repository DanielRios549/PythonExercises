from coin.utils.format import format


def increment(number: float, percent: int, coin: bool = False):
    result = number + (number * percent / 100)

    return format(result) if coin is True else result


def decrement(number: float, percent: int, coin: bool = False):
    result = number - (number * percent / 100)

    return format(result) if coin is True else result
