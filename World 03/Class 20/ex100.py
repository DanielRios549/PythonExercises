'''
    Create a list and two functions called raffle() and evenSum().
    The first will random five numbers and put inside a list.
    And the second will show the sum of all even values generated in the first function.
'''
from random import randint
from time import sleep

values = []


def raffle():
    print('Random \033[32m5 values\033[m to the list:', end=' ')

    for count in range(0, 5):
        value = randint(1, 20)
        values.append(value)
        print(f'\033[34m{value}\033[m', end=' ', flush=True)
        sleep(0.5)

    print('Done!')


def evenSun(numbers):
    even = []

    for number in numbers:
        if number % 2 == 0:
            even.append(number)

    print(f'The \033[32msum\033[m of even values in the list \033[34m{numbers}\033[m equals \033[32m{sum(even)}\033[m')


raffle()
evenSun(values)
