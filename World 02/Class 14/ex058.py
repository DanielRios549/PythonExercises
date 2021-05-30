'''
    Remake the Exercise 028, adding the feature to the player try until they guess right.
    In the end, show how many attempts was necessary to the player to guess right.
'''
from random import randint

computer = randint(1, 10)
print(computer)
player = int(input('Choose a number: '))
attempts = attempt = 1

if computer == player:
    print(f'\033[32mYOU WIN!\033[m Both chose the number \033[34m{computer}\033[m, you did that in only \033[34m{attempts}\033[m attempt.')
else:
    print(f'Wrong number, the computer do not chose the number \033[34m{player}\033[m.')
    again = input('Want to continue? [S/N] ').strip().upper()

    while again == 'S':
        attempt = int(input('Choose another number: '))
        attempts += 1

        if attempt != computer:
            print(f'Wrong number, the computer do not chose the number \033[34m{attempt}\033[m')
            more = input('Want to continue? [S/N] ').strip().upper()
            again = more
        else:
            again = 'N'

    if attempt == computer:
        print(f'\033[32mYOU WIN!\033[m You spent \033[34m{attempts}\033[m attempts to find out the number the computer chose (\033[34m{computer}\033[m)')
    else:
        print(f'\033[31mYOU LOSE!\033[m You spent \033[34m{attempts}\033[m attempts but do not find out the number the computer chose (\033[34m{computer}\033[m)')
