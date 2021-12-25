from coin.utils.format import format
import coin.calc.basic as basic
import coin.calc.percentage as percentage


def summary(number: float, increase: int = 10, decrease: int = 10):
    print(f'The half of \033[34m{format(number)}\033[m is \033[32m{basic.half(number, True)}\033[m')
    print(f'The double of \033[34m{format(number)}\033[m is \033[32m{basic.double(number, True)}\033[m')
    print(f'Increasing \033[34m{increase}%\033[m, the new price is \033[32m{percentage.increment(number, increase, True)}\033[m')
    print(f'Decreasing \033[34m{decrease}%\033[m, the new price is \033[32m{percentage.decrement(number, decrease, True)}\033[m')
