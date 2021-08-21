'''
    Create a game where 4 players plays a dice and get a random data, and put the data in a dict.
    In the end, show the dict ordered, knowing that the winner gets the highest number from the dice.
'''
from random import randint

players = dict()
scores = list()
width = 20
divisor = '-*'

for player in range(0, 4):
    dice = randint(1, 6) + randint(1, 6)

    if dice not in scores:
        scores.append(dice)

    if str(dice) not in players.keys():
        players[str(dice)] = [f'Player{player + 1}']
    else:
        players[str(dice)].append(f'Player{player + 1}')

    print(f'\033[32mPlayer{player + 1}\033[m gets \033[34m{dice}\033[m on dice.')

scores.sort(reverse=True)

print(divisor * width)
print(f'{"Ranking":^{len(divisor) * width}}')
print(divisor * width)

index = 0
current = 0

for score in scores:
    for player in players[str(score)]:
        current += 1
        index += 1

        if current != index:
            index += current

        print(f'{index}º Place: \033[32m{player}\033[m with \033[34m{score}\033[m points.')
