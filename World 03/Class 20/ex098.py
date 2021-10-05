'''
    Create a function called counter() that recieves three values,
    start, end and sal, and do the following:

    1 - From 1 to 10, one by one.
    2 - From 10 to 0, two by two.
    3 - A custom counting.
'''
from time import sleep


def divisor():
    division = '-='
    count = 20
    print(division * count)


def counter(add, interval, *numbers):
    divisor()
    duration = 0.3
    current = numbers[0]
    end = numbers[-1]
    print(f'From \033[31m{current}\033[m to \033[32m{end}\033[m (\033[34m{interval}\033[m by \033[34m{interval}\033[m)')
    sleep(2)

    # Increment

    while add is True and current <= end:
        print(f'\033[34m{current}\033[m', end=' ', flush=True)
        current += interval

        sleep(duration)

    # Decrement

    while add is False and current >= end:
        print(f'\033[34m{current}\033[m', end=' ', flush=True)
        current -= interval

        sleep(duration)

    print('The End!')
    divisor()


counter(True, 1, 1, 10)
counter(False, 2, 10, 0)

print('Now it is your turn to personalize the counter: ')

custom = (
    int(input(f'Start: ')),
    int(input(f'End: ')),
    abs(int(input('Interval: ')))
)
add = True if custom[0] < custom[1] else False

counter(
    add,
    custom[2],
    custom[0],
    custom[1]
)
