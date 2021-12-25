from coin.utils.format import format


def double(number: float, coin: bool = False):
    result = number * 2

    return format(result) if coin is True else result


def half(number: float, coin: bool = False):
    result = number / 2

    return format(result) if coin is True else result
