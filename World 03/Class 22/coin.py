def format(number: float):
    return f'R${number:.2f}'.replace('.', ',')


def increment(number: float, percent: int):
    return number + (number * percent / 100)


def decrement(number: float, percent: int):
    return number - (number * percent / 100)


def double(number: float):
    return number * 2


def half(number: float):
    return number / 2
