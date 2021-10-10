'''
    Exercise 099 made with lists and random values
'''

from random import randint
from time import sleep


def division():
    print('-=' * 30)


def highest(numbers):
    total = len(numbers)

    if total > 0:
        print(f'Analysing \033[32m{total}\033[m numbers...')
        sleep(1)

        for number in numbers:
            print(f'\033[34m{number}\033[m', end=' ', flush=True)
            sleep(0.5)

        print(f'\nThe highest value is \033[32m{max(numbers)}\033[m')
        division()
    else:
        print('There is \033[31mno numbers\033[m to analyse')


total = randint(1, 10)
print(f'It will be made \033[34m{total}\033[m comparisons.')
sleep(3)
division()

for item in range(0, total):
    items = []
    length = randint(0, 20)

    while len(items) <= length:
        items.append(randint(1, 200))

    highest(items)
