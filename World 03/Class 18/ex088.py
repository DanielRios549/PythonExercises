'''
    Help the user to guess the numbers of the lottery draw.
    Ask how many games will be played and generate 6 numbers from 1 to 60 for each one,
    put them in a list.
'''

from random import sample
from time import sleep

division = '-'
width = 40
print(f'{division * width}\n{"Mega Sena":^{width}}\n{division * width}')

games = int(input('How many games do you will play? '))

if games < 1:
    print('If you \033[32mdon\'t play\033[m, you \033[31mwon\'t have\033[m the chance of being a \033[34mmillionaire\033[m. Sorry.')

else:
    for game in range(0, games):
        if game == 0:
            print(f'I will random \033[34m{games}\033[m games for you. Let\'s Go!')
            print(division * width)
            sleep(2)

        numbers = sample(range(1, 61), 6)
        numbers.sort()

        print(f'\033[34mGame {game + 1}\033[m: {numbers}')
        sleep(1)

print('\033[32mGood Luck!\033[m')
