'''
    Make the computer plays jokenpo with you
'''
from random import choice
from emoji import emojize
from time import sleep

print(f'{"Rock-paper-scissors":=^40}')
options = [1, 2, 3]
computer = choice(options)
names = ['rock', 'paper', 'scissors']
icons = [':punch:', ':hand:', ':v:']

player = int(input('''
\033[34m[ 1 ]\033[m Rock
\033[34m[ 2 ]\033[m Paper
\033[34m[ 3 ]\033[m Scissors

Choose one: '''))

if player in options:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')

    # Define the name for each option

    p1 = names[computer - 1]
    p2 = names[player - 1]

    # Verify who win

    if computer == player:
        result = 'draw'
        print(emojize(f'{icons[computer - 1]:^14}|  {icons[player - 1]}', use_aliases=True))
    elif computer == 1 and player == 2:  # Computer rock, player paper
        result = 'player'
        verb = 'covers'
        print(emojize(f'{icons[0]:^14}|  {icons[1]}', use_aliases=True))
    elif computer == 1 and player == 3:  # Computer rock, player scissors
        result = 'computer'
        verb = 'is broke by'
        print(emojize(f'{icons[0]:^14}|  {icons[2]}', use_aliases=True))
    elif computer == 2 and player == 1:  # Computer paper, player rock
        result = 'computer'
        verb = 'is covered by'
        print(emojize(f'{icons[1]:^13}|  {icons[0]}', use_aliases=True))
    elif computer == 2 and player == 3:  # Computer paper, player scissors
        result = 'player'
        verb = 'cuts'
        print(emojize(f'{icons[1]:^13}|  {icons[2]}', use_aliases=True))
    elif computer == 3 and player == 1:  # Computer scissors, player rock
        result = 'player'
        verb = 'breaks'
        print(emojize(f'{icons[2]:^11}|  {icons[0]}', use_aliases=True))
    elif computer == 3 and player == 2:  # Computer scissors, player paper
        result = 'computer'
        verb = 'is cut buy'
        print(emojize(f'{icons[2]:^11}|  {icons[1]}', use_aliases=True))

    # Print the result

    if result == 'draw':
        print('Computer | You')
        print('\033[34mDraw!\033[m You both choose the same.')
    elif result == 'player':
        print('Computer | You')
        print(f'\033[32mYou win!\033[m \033[35m{p2}\033[m {verb} the \033[35m{p1}\033[m')
    elif result == 'computer':
        print('Computer | You')
        print(f'\033[31mYou lose!\033[m \033[35m{p2}\033[m {verb} the \033[35m{p1}\033[m')
    else:
        print('I ran into a problem! Try again, please.')
else:
    print('Choose a valid option, please.')
