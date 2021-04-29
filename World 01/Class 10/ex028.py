'''
    Make the computer choose one number from 0 to 5, and asks the user if they know what was the number.
    The script should print if the user wins of loses.
'''
from random import randint
from time import sleep

number = randint(0, 5)

print('\033[34m-=-\033[m' * 20)
print('I will choose a number from 0 to 5. Guess what?')
print('\033[34m-=-\033[m' * 20)

answer = int(input('What number did I choose? '))
print('\033[36mPROCESSING...\033[m')
sleep(3)

if number == answer:
    print(f'You win! I thought in the number \033[32m{number}\033[m')
else:
    print(f'You loose! I thought in the number\033[32m {number}\033[m and not in the \033[31m{answer}\033[m')
