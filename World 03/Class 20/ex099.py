'''
    Create a function called highest() that receives integers values.
    You need to analyse all values and show the highest of them.
'''

from time import sleep


def division():
    print('-=' * 30)


def highest(*numbers):
    total = len(numbers)

    if total > 0:
        print(f'Analysing \033[32m{total}\033[m numbers...')
        sleep(2)

        for number in numbers:
            print(f'\033[34m{number}\033[m', end=' ', flush=True)
            sleep(0.5)

        print(f'\nThe highest value is \033[32m{max(numbers)}\033[m')
        division()
    else:
        print('There is \033[31mno numbers\033[m to analyse')


highest(9, 5, 2, 0, 3, 2)
highest(20, 5, 2, 1, 76, 8, 2, 9, 8)
highest(7, 4, 9, 1)
highest(8)
highest()
